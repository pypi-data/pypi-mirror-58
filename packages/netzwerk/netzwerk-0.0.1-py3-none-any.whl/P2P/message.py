# © 2019 Noel Kaczmarek
import json


class Message:
    def __init__(self, author, data, type='message'):
        if type == 'message':
            self.data = json.dumps(data)
        elif type == 'bytes':
            self.data = data

        self.header = {'author': author, 'length': len(self.data), 'type': type}

    def GetHeader(self):
        return self.header

    def GetData(self):
        return self.data