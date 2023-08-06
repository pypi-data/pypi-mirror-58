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
