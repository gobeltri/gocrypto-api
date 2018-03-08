import http.server
import socketserver

PORT = 8080

def run_http_server():
    Handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer(("", PORT), Handler)
    print("Serving at port", PORT)
    httpd.serve_forever()
    