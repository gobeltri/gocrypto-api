from http.server import HTTPServer, BaseHTTPRequestHandler
import time

HOSTNAME = ''
PORT = 8080


# Override SimpleHTTPRequestHandler to serve GET requests
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello, goworld!')
    

def run_goserver(hostname, port):
    httpd = HTTPServer((hostname, port), SimpleHTTPRequestHandler)
    print(time.asctime(), "Server Starts - %s:%s" % (hostname, port))

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print(time.asctime(), "Server Stops - %s:%s" % (hostname, port))


if __name__ == "__main__":
	run_goserver(HOSTNAME, PORT)    