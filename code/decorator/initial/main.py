import stream.filestream.filestream
import stream.memorystream.memorystream
import stream.networkstream.networkstream

fileStream = stream.filestream.filestream.FileStream()
fileStream.read()
fileStream.seek()
fileStream.write()

memoryStream = stream.memorystream.memorystream.MemoryStream()
memoryStream.read()
memoryStream.seek()
memoryStream.write()

networkStream = stream.networkstream.networkstream.NetworkStream()
networkStream.read()
networkStream.seek()
networkStream.write()
