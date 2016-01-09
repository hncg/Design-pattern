# coding=utf-8


class FactoryModel(object):

    def __getattr__(self, attribute):
        try:
            func = object.__getattribute__(self, 'get_{}'.format(attribute)) # noqa
            value = func()
            setattr(self, attribute, value)
        except:
            value = None
            setattr(self, attribute, value)
        return value

    def get_cgg(self):
        return 1

    def get_cgg2(self):
        return self.cgg + 1


class Test(FactoryModel):

    def __init__(self):
        pass

    def serialize(self):
        return self

test = Test().serialize()
print test.cgg2
print '-----------'
print test.cgg
