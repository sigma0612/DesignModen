from .. import stream


class FileStream(stream.Stream):
    def read(self):
        print("FileStream read...")

    def seek(self):
        print("FileStream seek...")

    def write(self):
        print("FileStream write...")