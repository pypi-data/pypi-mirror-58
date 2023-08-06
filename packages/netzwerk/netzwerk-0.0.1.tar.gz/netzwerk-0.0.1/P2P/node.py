# © 2019 Noel Kaczmarek
from P2P.connection import Connection
from P2P.message import Message

import threading
import socket
import json
import time
import uuid
import os


class Node(threading.Thread):
    def __init__(self, host, port):
        super(Node, self).__init__()

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.terminate_flag = threading.Event()
        self.id = uuid.uuid4().int
        self.host = host
        self.port = port
        self.nodesIn = []
        self.nodesOut = []

        print('Host: %s, Port: %s, ID: %s' % (self.host, self.port, self.id))

        self.InitialiseServer()

    def InitialiseServer(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind(('', self.port))
        self.sock.settimeout(10.0)
        self.sock.listen(1)

    def Connect(self, host, port):
        if (host == self.host and port == self.port):
            return;

        for node in self.nodesOut:
            if (node.GetHost() == host and node.GetPort() == port):
                print('Connect: Already connected to this node.')
                return True

        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print('Connecting to %s port %s...' % (host, port))
            sock.connect((host, port))

            client_thread = Connection(self, sock, (host, port))
            client_thread.start()
            client_thread.Send({'type': 'InitialTransmission', 'ID': self.id, 'port': self.port})
            self.nodesOut.append(client_thread)
            self.PrintConnections()

        except Exception as e:
            print('TcpServer.connect_with_node: Could not connect with node. (' + str(e) + ')')

    def Disconnect(self, node):
        if node in self.nodesOut:
            node.Send({'type': 'TerminationSignal'}) # Update this line
            node.stop()
            node.join()
            del self.nodesOut[self.nodesOut.index(node)]

    def Leave(self):
        self.Broadcast({'type': 'LeaveRequest'})

    def Broadcast(self, data, exclude=[]):
        for node in self.nodesIn:
            if node not in exclude:
                self.SendToNode(node, data)

        for node in self.nodesOut:
            if node not in exclude:
                self.SendToNode(node, data)

    def SendToNode(self, node, data):
        if node in self.nodesIn or node in self.nodesOut:
            node.Send(data)
        else:
            print('SendToNode: Could not send the data, node is not found!')

    def SendRoutingTable(self, exclude=[]):
        nodesIn = []
        nodesOut = []

        for node in self.nodesIn:
            id = node.GetID()
            host = node.GetHost()
            port = node.GetPort()

            nodesIn.append({'ID': id, 'host': host, 'port': port})

        for node in self.nodesOut:
            id = node.GetID()
            host = node.GetHost()
            port = node.GetPort()

            nodesOut.append({'ID': id, 'host': host, 'port': port})

        self.Broadcast({'type': 'RoutingTableUpdate', 'IncomingConnections': nodesIn, 'OutgoingConnections': nodesOut}, exclude)

    def run(self):
        while not self.terminate_flag.is_set():
            try:
                connection, client_address = self.sock.accept()

                thread_client = Connection(self, connection, client_address)
                thread_client.start()
                self.nodesIn.append(thread_client)
                self.PrintConnections()

            except socket.timeout:
                pass

            except KeyboardInterrupt:
                os._exit(0)

            except:
                raise

            time.sleep(0.01)

        print('Node stopping...')

        for t in self.nodesIn:
            t.stop()

        for t in self.nodesOut:
            t.stop()

        time.sleep(1)

        for t in self.nodesIn:
            t.join()

        for t in self.nodesOut:
            t.join()

        self.sock.close()

        print('Node stopped')

    def stop(self):
        self.terminate_flag.set()

    def PrintConnections(self):
        print('Connections:')
        print('- Total incoming connections: %d' % len(self.nodesIn))
        print('- Total outgoing connections: %d' % len(self.nodesOut))

    def RemoveNodeFromTable(self, id):
        for node in self.nodeServer.nodesIn:
            if node['ID'] == id:
                self.nodeServer.nodesIn.remove(node)

        for node in self.nodeServer.nodesOut:
            if node['ID'] == id:
                self.nodeServer.nodesOut.remove(node)

    def IsConnectedTo(self, id):
        if id in self.nodesIn or self.nodesOut:
            return True
        else:
            return False

    def GetNodeInfo(self):
        return {'ID': self.id, 'port': self.port, 'IncomingConnections': len(self.nodesIn), 'OutgoingConnections': len(self.nodesOut)}

    def GetHost(self):
        return self.host

    def GetPort(self):
        return self.port

    def GetRoutingTable(self):
        return self.peers

    def GetID(self):
        return self.id