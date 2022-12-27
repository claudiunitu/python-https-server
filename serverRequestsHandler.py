from http.server import BaseHTTPRequestHandler

import os


class HandleRequests(BaseHTTPRequestHandler):
    
                    
    def _set_headers(self, responseCode, message, contentType):
        self.send_response(responseCode, message)
        self.send_header('Content-type', contentType)
        self.send_header("Access-Control-Allow-Origin","*")
        self.send_header("Access-Control-Allow-Methods","*")
        self.send_header("Access-Control-Allow-Headers","*")
        self.end_headers()

    def getServedStorageContentType(self, path: str):
        extension = path.split(".")
        if(len(extension) <= 1):
            return 'text/plain'
        else:
            match extension[len(extension)-1].lower():
                case "html":
                    return "text/html"
                case "json":
                    return "application/json"
                case "js":
                    return "text/javascript"
                case "css":
                    return "text/css"
                case _:
                    return "text/plain"


    def serveStorageContent(self, baseHTTPRequestHandler, path: str ):
        path = path.split('?')[0]
        if path == "/":
            path = "/index.html"
        try:
            file_to_serve = open('./storage'+path, 'rb')
            
            self._set_headers(200, "OK", self.getServedStorageContentType(path))
            baseHTTPRequestHandler.wfile.write(file_to_serve.read())
            file_to_serve.close()
        except Exception as e:
            self._set_headers(501, "Generic Error", "text/plain")
        

    def do_OPTIONS(self):
        self._set_headers(200, "OK", "text/plain")

    def do_HEAD(self):
        self._set_headers(200, "OK", "text/plain")


    def do_GET(self):
        
        path = self.path
        print(path)
        self.serveStorageContent(self, path)
        
    
    def do_POST(self):
        print("received put request")
        
        path = self.path

        filename = 'test.txt'
        if os.path.exists(filename):
            self._set_headers(409, 'Conflict', "text/plain")
            reply_body = '"%s" already exists\n' % filename
            self.wfile.write(reply_body.encode('utf-8'))
            
            return

        file_length = int(self.headers['Content-Length'])
        read = 0
        with open(filename, 'wb+') as output_file:
            while read < file_length:
                new_read = self.rfile.read(min(66556, file_length - read))
                read += len(new_read)
                output_file.write(new_read)
        self._set_headers(201, 'Created', "text/plain")
        reply_body = 'Saved "%s"\n' % filename
        self.wfile.write(reply_body.encode('utf-8'))
        