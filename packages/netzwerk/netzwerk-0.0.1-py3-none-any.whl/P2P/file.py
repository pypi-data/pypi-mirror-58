# © 2019 Noel Kaczmarek
import os


class Shard:
    def __init__(self, filepath, offset, index, size, data):
        print('Creating shard...')
        self.file = filepath
        self.offset = offset
        self.index = index
        self.size = size
        self.data = data

    def Read(self):
        with open(self.file, 'rb') as file:
            file.seek(self.offset, 0)
            content = file.read(self.size)
            file.close()

        return content

    def Write(self):
        with open(self.file, 'wb') as file:
            file.seek(0, 0)
            file.write(self.data)
            file.close()

    def GetFile(self):
        return self.file

    def GetOffset(self):
        return self.offset

    def GetIndex(self):
        return self.index

    def GetSize(self):
        return self.size

    def GetData(self):
        return self.data


class File:
    def __init__(self, filepath):
        self.file = filepath
        self.size = os.stat(self.file).st_size
        self.shards = []
        print('File name: %s, File size: %d' % (self.file, self.size))

    def Read(self, bytes=0, offset=0):
        with open(self.file, 'rb') as file:
            file.seek(offset, 0)
            content = file.read(bytes)
            file.close()

        return content

    def Split(self):
        shard_size = round(self.size / 4)
        print('Shard size: %d' % shard_size)
        n = 0

        while n < 4:
            data = self.Read(shard_size, shard_size * n)
            self.shards.append(Shard('%d_%s.shard' % (n, self.file), shard_size * n, n, shard_size, data))
            n += 1

        for shard in self.shards:
            shard.Write()

    def Weld(self):
        print('Welding file together...')
        file = open('welded_' + self.file, 'wb')
        
        for shard in self.shards:
            file.seek(shard.offset, 0)
            file.write(shard.GetData())

        file.close()