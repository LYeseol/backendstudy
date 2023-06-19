from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200, 'OK')
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()
        #web sorket에 파일처럼 쓰는
        self.wfile.write(b"Hello World")

server = HTTPServer(("", 8080), SimpleHTTPRequestHandler)

server.serve_forever()