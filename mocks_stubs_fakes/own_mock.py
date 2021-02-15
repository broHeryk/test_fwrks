

class OwnAttr:
    def __init__(self):
        self.call_count = 0
        self.call_args_kwargs = []

    def __call__(self, *args, **kwargs):
        self.call_count += 1
        self.call_args_kwargs.append((args, kwargs,))


class OwnMock:
    def __getattr__(self, item):
        if item not in self.__dict__:
            attr = OwnAttr()
            self.__setattr__(item, attr)

        return self.__dict__[item]
