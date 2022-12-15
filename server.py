import socket

from http.server import HTTPServer
import ssl

from serverRequestsHandler import HandleRequests


SERVER_HOST_NAME = socket.gethostname()
SERVER_HOST_IP = socket.gethostbyname(SERVER_HOST_NAME)
SERVER_PORT = 4433

USE_TLS = True

def startServer():
  s = HTTPServer((SERVER_HOST_IP, SERVER_PORT), HandleRequests)

  if USE_TLS:
    s.socket = ssl.wrap_socket (s.socket, 
    keyfile="./server-security/key.pem", 
    certfile='./server-security/cert.pem', server_side=True, ssl_version=ssl.PROTOCOL_TLS)

  print(SERVER_HOST_IP)
  s.serve_forever()








if __name__ == '__main__':
  startServer()
