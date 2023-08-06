from typing import Dict, Callable, Any, Set, Union, Type

BeanRef = Union[str, Type]


class BeanFactory:
    def __init__(self, factory_func: Callable[..., Any]):
        self.factory_func = factory_func

    def create_bean(self, dependencies):
        return self.factory_func(**dependencies)


class BeanDef:
    def __init__(self,
                 bean_id: str,
                 bean_factory: BeanFactory,
                 dependencies: Dict[str, BeanRef],
                 profile_func: Callable[[Set[str]], bool]):
        self.profile_func = profile_func
        self.dependencies = dependencies
        self.bean_factory = bean_factory
        self.bean_id = bean_id
