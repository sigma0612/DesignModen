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


class FileStream(Stream):
    def write(self):
        print("filestream write...")

    def read(self):
        print("filestream read...")

    def seek(self):
        print("filestream seek...")


class NetworkStream(Stream):
    def write(self):
        print("NetworkStream write...")

    def read(self):
        print("NetworkStream read...")

    def seek(self):
        print("NetworkStream seek...")


class MemoryStream(Stream):
    def write(self):
        print("MemoryStream write...")

    def read(self):
        print("MemoryStream read...")

    def seek(self):
        print("MemoryStream seek...")


class CryptoStream(Stream):
    def __init__(self, stream: Stream):
        self.stream = stream

    def write(self):
        print("加密")
        self.stream.write()
        print("加密")

    def read(self):
        print("加密")
        self.stream.read()
        print("加密")

    def seek(self):
        print("加密")
        self.stream.seek()
        print("加密")


class BufferedStream(Stream):
    def __init__(self, stream: Stream):
        self.stream = stream

    def write(self):
        print("缓冲")
        self.stream.write()
        print("缓冲")

    def read(self):
        print("缓冲")
        self.stream.read()
        print("缓冲")

    def seek(self):
        print("缓冲")
        self.stream.seek()
        print("缓冲")
