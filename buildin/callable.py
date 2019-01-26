print(callable(max))


class C(object):
    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):
        pass


print(callable(C))
print(callable(C()))
