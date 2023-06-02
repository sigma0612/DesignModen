from abc import abstractmethod


class Stream:
    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def seek(self):
        pass

    @abstractmethod
    def write(self):
        pass
