class QueryRow(dict):
    def __init__(self, keys, values):
        arg_zip = zip(keys, values)
        super().__init__(dict(arg_zip))
        for key, value in arg_zip:
            try:
                getattr(self, key)
                key = f'{key}_'
            except AttributeError:
                pass
            setattr(self, key, value)


"""
class DotNotationObject:
    def __init__(self, obj: dict):
        self.__obj = obj
        for key, value in zip(self.__obj.keys(), self.__obj.values()):
            setattr(self, key, value)

    def items(self):
        return self.__obj.items()

    def __getitem__(self, key):
        try:
            value = self.__obj[key]
            return value
        except AttributeError:
            raise KeyError(f'key {key!r} not found')

    def get(self, item):
        return getattr(self, item, None)

    def keys(self):
        return self.__obj.keys()

    def values(self):
        return self.__obj.values()

    def pop(self, key, default='__None'):
        value = self.get(key)
        if not value:
            if default == '__None':
                raise KeyError(key)
            else:
                return default
        else:
            delattr(self, key)
            self.__obj.pop(key)
            return value

    def popitem(self):
        try:
            item = self.__obj.popitem()
            delattr(self, item[0])
            return item
        except KeyError as err:
            return ()
"""