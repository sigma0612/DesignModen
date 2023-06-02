import stream.stream

Stream = stream.stream.Stream()

FileStream = stream.stream.FileStream()
NetworkStream = stream.stream.NetworkStream()

CryptoStream = stream.stream.CryptoStream(FileStream)
BufferedStream = stream.stream.BufferedStream(NetworkStream)

CryptoStream.seek()
BufferedStream.read()
