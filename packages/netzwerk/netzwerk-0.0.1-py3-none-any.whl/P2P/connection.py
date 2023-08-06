# © 2019 Noel Kaczmarek
from P2P.message import Message
from P2P.vars import HEADER_SIZE

import threading
import socket
import json


class Connection(threading.Thread):
    def __init__(self, nodeServer, sock, clientAddress):
        super(Connection, self).__init__()

        self.id = 0
        self.sock = sock
        self.host = clientAddress[0]
        self.port = clientAddress[1]
        self.nodeServer = nodeServer
        self.clientAddress = clientAddress
        self.terminate_flag = threading.Event()

    def Send(self, data):
        try:
            message = Message(self.nodeServer.GetID(), data)

            self.sock.sendall(json.dumps(message.GetHeader()).encode('utf-8'))
            self.sock.sendall(message.GetData().encode('utf-8'))
        except Exception as e:
            print('Connection.Send: Unexpected error:' + e)
            self.terminate_flag.set()

    def stop(self):
        self.terminate_flag.set()

    def run(self):
        while not self.terminate_flag.is_set():
            header = json.loads(self.sock.recv(HEADER_SIZE))
            data = self.sock.recv(int(header['length'])).decode('utf-8')

            # print('Header: %s' % header)
            # print('Data: %s' % data)

            if header['type'] == 'message':
                data = json.loads(data)

                if data['type'] == 'InitialTransmission':
                    self.id = data['ID']
                    self.port = data['port']
                    self.nodeServer.SendRoutingTable()

                    # print('ID: %s, Port: %d' % (self.id, self.port))

                elif data['type'] == 'LeaveRequest':
                    self.nodeServer.RemoveNodeFromTable(header['author'])

                elif data['type'] == 'RoutingTableUpdate':
                    for node in data['IncomingConnections']:
                        if node['ID'] != self.nodeServer.GetID():
                            self.nodeServer.Connect(node['host'], node['port'])

                    for node in data['OutgoingConnections']:
                        if node['ID'] != self.nodeServer.GetID():
                            self.nodeServer.Connect(node['host'], node['port'])

    def GetID(self):
        return self.id

    def GetHost(self):
        return self.host

    def GetPort(self):
        return self.port
