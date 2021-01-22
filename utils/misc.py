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


def convert_time(seconds):
    n = seconds // (60 * 60)
    if n:
        return f'{int(n)} hour(s)'
    n = seconds // 60
    if n:
        return f'{int(n)} minute(s)'
    return f'{int(seconds)} second(s)'


def truncate(text, length):
    return f'{text[:length]}{"..." if length < len(text) else ""}'
