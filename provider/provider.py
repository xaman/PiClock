class Provider(object):
    def initialize(self):
        raise NotImplementedError("Class %s doesn't implement initialize()" % self.__class__.__name__)

    def is_empty(self):
        raise NotImplementedError("Class %s doesn't implement is_empty()" % self.__class__.__name__)

    def get_value(self):
        raise NotImplementedError("Class %s doesn't implement get_value()" % self.__class__.__name__)
