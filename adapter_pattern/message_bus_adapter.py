
class ProxyAdapter(object):
    def __init__(self, MessageBusBrokerAdaptee):
        self.messageBusBrokerAdaptee = MessageBusBrokerAdaptee

    def say_hello(self):
        self.messageBusBrokerAdaptee(1).say_hello()


class Adapter(object):
    def __init__(self, obj, adapted_methods):
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __getattr__(self, attr):
        return getattr(self.obj, obj)