from typing import Set, Callable, Dict

from pybeandi.model import BeanRef


def bean(bean_id: str,
         profiles: Set[str] = None,
         profile_func: Callable[[Set[str]], bool] = lambda profs: True,
         **depends_on: Dict[str, BeanRef]):
    def wrapper(cls):
        cls._depends_on = depends_on
        cls._bean_id = bean_id

        if profiles is None:
            cls._profile_func = profile_func
        else:
            cls._profile_func = lambda profs: profs >= profiles

        return cls

    return wrapper
