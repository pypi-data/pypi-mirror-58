import warnings
from functools import wraps

from abconfig.common import Dict


class Settings:
    __settings__ = (
        '__prefix__',
        '__hidesettings__',
        '__file_required__',
        '__file__',
        '__env__',
        '__vault__',
    )

    __hidesettings__ = True
    __file_required__ = False
    __file__ = False
    __env__ = True
    __prefix__ = None
    __vault__ = False


class HideSettings(Dict):
    __exclude__ = ['__prefix__']

    def __init__(self, obj: Dict):
        if obj.get('__hidesettings__', True) is True:
            for k,v in dict(obj).items():
                if k in Settings.__settings__ and \
                        not k in self.__exclude__ or not v:
                    obj.pop(k)
        super().__init__(obj)


class Close(Dict):
    def __init__(self, obj: Dict):
        super().__init__(Dict(obj).fmap(self.set_default_type))

    @staticmethod
    def set_default_type(k, v):
        if Dict.is_dict(v):
            return (k, Close(v))
        elif Dict.is_list(v):
            return (k, Dict.is_type(v)([None if isinstance(i, type) else i for i in v]))
        else:
            return (k, None if isinstance(v, type) else v)


def ignore_warnings(f):
    @wraps(f)
    def inner(*args, **kwargs):
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("ignore")
            response = f(*args, **kwargs)
        return response
    return inner
