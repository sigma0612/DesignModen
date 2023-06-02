from .. import stream


class NetworkStream(stream.Stream):
    def read(self):
        print("NetworkStream read...")

    def seek(self):
        print("NetworkStream seek...")

    def write(self):
        print("NetworkStream write...")
