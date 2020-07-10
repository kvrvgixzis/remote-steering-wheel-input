from message import Message, MessageSerializer
from threading import Lock
import logging
import socket
import time

logging.basicConfig(format='\033[94m[%(asctime)s][%(levelname)s]\033[0m %(message)s', level=logging.INFO)


class SocketClient(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = None
        self.mutex = Lock()
        self.__connect()
        self.start()

    def __connect(self):
        if self.socket:
            self.socket.close()

        while True:
            try:
                logging.info(f'Connect to "{self.host}:{self.port}"')
                self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
                self.socket.connect((self.host, self.port))
                break
            except Exception as e:
                logging.info('Server down. Try reconnect...')
                time.sleep(1)

    def __recvall(self):
        message = None
        try:
            data = b''
            while True:
                part = self.socket.recv(1)
                data += part
                if bytes([data[-1]]) == bytes([255]):
                    break
            message = MessageSerializer.deserialize(data)
        except Exception as e:
            logging.info(f'server down. reconnecting...')
            self.__connect()
        finally:
            return message

    def start(self):
        while True:
            logging.info(self.__recvall())


if __name__ == '__main__':
    sc = SocketClient(host='tech.splinex-team.com', port=5000)
