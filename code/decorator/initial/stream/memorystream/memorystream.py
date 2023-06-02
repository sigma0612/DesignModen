from .. import stream


class MemoryStream(stream.Stream):
    def read(self):
        print("MemoryStream read...")

    def seek(self):
        print("MemoryStream seek...")

    def write(self):
        print("MemoryStream write...")
