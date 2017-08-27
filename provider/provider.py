class Provider(object):
    def __init__(self):
        self.data = None
        self.formatter = None

    def initialize(self):
        raise NotImplementedError("Class %s doesn't implement initialize()" % self.__class__.__name__)

    def is_empty(self):
        return self.data is None

    def get_value(self):
        return self.data

    def get_formatted_value(self):
        return self.formatter.format(self.data)
