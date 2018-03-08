from http.server import HTTPServer, BaseHTTPRequestHandler
import time
from gocrypto_fees import build_fees_list
import json

HOSTNAME = ''
PORT = 8080


# Override SimpleHTTPRequestHandler to serve GET requests
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        
        # Response ok
        self.send_response(200)
        
        # JSON Header
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        
        # Print list
        currencies = build_fees_list()
        content = json.dumps(currencies)
        body = content.encode('UTF-8', 'replace')
        self.wfile.write(body)
        

def run_goserver(hostname, port):
    httpd = HTTPServer((hostname, port), SimpleHTTPRequestHandler)
    print(time.asctime(), "Server Starts - %s:%s" % (hostname, port))

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print(time.asctime(), "Server Stops - %s:%s" % (hostname, port))


if __name__ == "__main__":
	run_goserver(HOSTNAME, PORT)