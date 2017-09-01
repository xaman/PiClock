class Formatter(object):
    def format(self, value):
        raise NotImplementedError("Class %s doesn't implement format()" % self.__class__.__name__)
