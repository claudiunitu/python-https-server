import socket

from http.server import HTTPServer
import ssl

from serverRequestsHandler import HandleRequests


SERVER_HOST_NAME = socket.gethostname()
SERVER_HOST_IP = socket.gethostbyname(SERVER_HOST_NAME)
SERVER_PORT = 4433

USE_TLS = False

def startServer():
  s = HTTPServer((SERVER_HOST_IP, SERVER_PORT), HandleRequests)

  if USE_TLS:
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile="./server-security/cert.pem", keyfile="./server-security/key.pem")
    s.socket = context.wrap_socket(s.socket, server_side=True)
  

  print(SERVER_HOST_IP)
  s.serve_forever()








if __name__ == '__main__':
  startServer()
