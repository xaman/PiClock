class Scroller(object):
    def show_clock(self):
        raise NotImplementedError("Class %s doesn't implement show_clock()" % self.__class__.__name__)

    def show_text(self, text):
        raise NotImplementedError("Class %s doesn't implement show_text()" % self.__class__.__name__)
