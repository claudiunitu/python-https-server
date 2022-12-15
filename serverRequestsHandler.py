from http.server import BaseHTTPRequestHandler


class HandleRequests(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        print("received get request")
        self._set_headers()
        path = self.path
        self.wfile.write(b"received get request: " + path.encode('utf-8'))
        