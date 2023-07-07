from http.server import HTTPServer, BaseHTTPRequestHandler
from wsgiref.simple_server import make_server

def application(envir, start_response):
    response_body = b"Hello world"

    status = "200 Ok"
    headers =[("Content-Type", "text/plain")]

    start_response(status, headers)
    return [response_body]


if __name__=='__main__':
    #server위에 내가 만든 application얹기
    httpd = make_server("", 8000, application)
    print("Running....")
    httpd.serve_forever()

# class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
#     def do_GET(self):
#         self.send_response(200, 'OK')
#         self.send_header('Content-Type', 'text/plain')
#         self.end_headers()
#         #web sorket에 파일처럼 쓰는
#         self.wfile.write(b"Hello World")
#
# server = HTTPServer(("", 8080), SimpleHTTPRequestHandler)
#
# server.serve_forever()