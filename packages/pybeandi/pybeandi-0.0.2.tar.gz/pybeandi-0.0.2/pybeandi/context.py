import inspect
from typing import Dict, Any, Callable, Type, Set, Union, List

import yaml

from pybeandi.errors import NoSuchBeanError, MultipleBeanInstancesError, ContextInitError, BeanIdAlreadyExistsError
from pybeandi.model import BeanDef, BeanFactory, BeanRef


class BeansList:
    """
    Readonly dictionary-like object to access beans
    """

    def __init__(self, beans=None):
        if beans is None:
            beans = {}
        self._beans = beans

    def get_bean(self, bean_ref: Union[str, Type]) -> Any:
        """
        Return bean from context by its id or class
        @param bean_ref: id or class of bean
        @return: bean
        @raise NoSuchBeanError: if such bean does not exist
        @raise MultipleBeanInstancesError: if more than one beans exist that satisfied given reference
        (for example multiple instances of class or it subclasses)
        """
        if type(bean_ref) is str:
            return self.get_bean_by_id(bean_ref)
        elif inspect.isclass(bean_ref):
            return self.get_bean_by_class(bean_ref)
        else:
            raise NoSuchBeanError(f'Invalid bean_ref param: {bean_ref}')

    def get_bean_by_id(self, bean_id: str) -> Any:
        """
        Return bean from context by its id
        @param bean_id: id of bean
        @return: bean
        @raise NoSuchBeanError: if such bean does not exist
        """
        if bean_id not in self._beans:
            raise NoSuchBeanError(f'Bean with id \'{bean_id}\' does not exist')
        return self._beans[bean_id]

    def get_bean_by_class(self, cls: Type) -> Any:
        """
        Return bean from context by its class
        @param cls: class of bean
        @return: bean
        @raise NoSuchBeanError: if such bean does not exist
        @raise MultipleBeanInstancesError: if more than one beans exist that satisfied given reference
        (for example multiple instances of class or it subclasses)
        """
        beans = {bean_id: bean for (bean_id, bean) in self._beans.items() if issubclass(type(bean), cls)}
        if len(beans) == 0:
            raise NoSuchBeanError(f'Bean of class \'{cls.__name__}\' does not exist')
        elif len(beans) > 1:
            raise MultipleBeanInstancesError(f'There are more than one instances of class \'{cls.__name__}\': '
                                             f'{", ".join(beans.keys())}')
        return list(beans.values())[0]

    def _add_as_bean(self, bean_id: str, obj: Any) -> None:
        """
        Register obj as bean
        @param bean_id: id of new bean
        @param obj: object to register as a bean
        """
        if bean_id in self._beans:
            raise BeanIdAlreadyExistsError(f'Bean with id \'{bean_id}\' already exists')
        self._beans[bean_id] = obj

    def __contains__(self, bean_ref: BeanRef):
        """
        Checks do bean exists by its reference
        @param bean_ref: reference
        @return: do bean exists
        """
        try:
            self.get_bean(bean_ref)
        except NoSuchBeanError:
            return False
        except MultipleBeanInstancesError:
            return True
        return True

    def __getitem__(self, bean_ref):
        return self.get_bean(bean_ref)

    def __len__(self):
        return len(self._beans)

    def __iter__(self):
        return iter(self._beans)

    def __str__(self):
        return str(self._beans)


class BeanContext:
    def __init__(self, bean_defs: List[BeanDef], profiles: Set[str]):
        self._bean_defs: List[BeanDef] = bean_defs
        self._beans: BeansList = BeansList()
        self._profiles = profiles

    @property
    def beans(self):
        return self._beans

    @property
    def profiles(self):
        return self._profiles

    def init(self) -> None:
        """
        Initialize context using bean definitions provided earlier
        @raise ContextInitError: is context incorrect
        """
        self._bean_defs = [bean_def for bean_def in self._bean_defs if bean_def.profile_func(self.profiles)]

        bean_ids = [bean_def.bean_id for bean_def in self._bean_defs]
        duplicate_ids = set([x for x in bean_ids if bean_ids.count(x) > 1])
        if len(duplicate_ids) > 0:
            raise ContextInitError(f'Multiple beans with same id exist: {", ".join(duplicate_ids)}')

        while any((bean_def.bean_id not in self.beans for bean_def in self._bean_defs
                   if bean_def.profile_func(self.profiles))):

            to_init = [bean_def for bean_def in self._bean_defs
                       if bean_def.profile_func(self.profiles)
                       and bean_def.bean_id not in self.beans
                       and all((bean_ref in self.beans for bean_ref in bean_def.dependencies.values()))]

            if len(to_init) == 0:
                raise ContextInitError(f'Circular or missing dependency was founded')

            for bean_def in to_init:
                bean = bean_def.bean_factory.create_bean({arg_name: self.beans[arg_bean_ref]
                                                          for (arg_name, arg_bean_ref)
                                                          in bean_def.dependencies.items()})
                self.beans._add_as_bean(bean_def.bean_id, bean)


class BeanContextBuilder:
    def __init__(self):
        self.bean_defs: List[BeanDef] = []
        self.profiles = set()

    def init(self) -> BeanContext:
        ctx = BeanContext(self.bean_defs, self.profiles)
        ctx.init()
        return ctx

    def load_yaml(self, file_path: str) -> None:
        """
        Load configuration from specified file
        @param file_path: YAML config file
        """
        with open(file_path, 'r', encoding='utf-8') as file:
            conf_raw = yaml.safe_load(file)
            if 'pybeandi' not in conf_raw:
                return
            conf = conf_raw['pybeandi']

            if 'profiles' in conf and 'active' in conf['profiles']:
                for profile in conf['profiles']['active']:
                    self.profiles.add(profile)
            if 'beans' in conf:
                for bean in conf['beans'].items():
                    bean_id, bean_obj = bean
                    self.add_as_bean(bean_id, bean_obj)

    def scan(self, globalns) -> None:
        """
        Scan provided namespace for beans
        @param globalns: result of globals() function
        """
        for cls in (x for x in globalns.values()
                    if (inspect.isclass(x) or callable(x))
                       and '_bean_id' in vars(x)):
            self.register_bean_by_class(cls)

    def register_bean(self,
                      bean_id: str,
                      factory_func: Callable[..., Any],
                      dependencies: Dict[str, BeanRef],
                      profile_func: Callable[[Set[str]], bool] = lambda profs: True) -> None:
        """
        Register bean to be created at init phase
        @param bean_id: id of registered bean
        @param factory_func: function or class that returns object of bean
        @param dependencies: dictionary of names of factory_func arg to reference to bean
        @param profile_func: function that returns do context need to create bean
        """
        self.bean_defs.append(BeanDef(bean_id, BeanFactory(factory_func), dependencies, profile_func))

    def register_bean_by_class(self, cls: Type) -> None:
        """
        Register bean to be created at init phase by class
        Class must be decorated by @bean first!
        @param cls: class of bean
        """
        self.register_bean(cls._bean_id, cls, cls._depends_on, cls._profile_func)

    def add_as_bean(self, bean_id: str, bean_obj: Any):
        self.register_bean(bean_id, lambda: bean_obj, {})
