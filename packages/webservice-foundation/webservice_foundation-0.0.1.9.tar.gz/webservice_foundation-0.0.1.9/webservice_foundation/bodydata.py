class BodyData(dict):

    def __init__(self, data):
        for k, v in data.items():
            self[k] = v
            setattr(self, k, v)

    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise ValueError('Key must be string.')
        return super(BodyData, self).__setitem__(key, value)

    def __getitem__(self, key):
        try:
            return super(BodyData, self).__getitem__(key)
        except:
            return None


class ConcatBodyData(dict):
    BODY = 'body'
    BODY_ARGS = 'body_args'
    QUERY_ARGS = 'query_args'

    def __init__(self, iterable):
        super(ConcatBodyData, self).__init__(iterable)

    def get(self, key, default=None):
        _keyerror = None

        def _get(parent_key):
            try:
                return self[parent_key].get(key)
            except KeyError as e:
                _keyerror = e
                return None
        data = _get(self.BODY)
        if data:
            return data
        data = _get(self.BODY_ARGS)
        if data:
            return data
        data = _get(self.QUERY_ARGS)
        if data:
            return data
        if default:
            return default
        return None
