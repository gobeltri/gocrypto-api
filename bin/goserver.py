from http.server import HTTPServer, BaseHTTPRequestHandler
import time
import json
import os
from gocrypto_fees import build_fees_list


# Working both in C9 && Heroku
HOSTNAME = os.environ.get('IP', '0.0.0.0')
PORT = int(os.environ.get('PORT', '8080'))
API_PATH = '/api/v1'


# Override SimpleHTTPRequestHandler to serve GET requests
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        
        # Accepting connections on /api/v1
        if self.path != API_PATH:
            self.send_response(200)
            self.end_headers()
            content = "<b>Welcome cypherpunk!</b>"
            body = content.encode('UTF-8', 'replace')
            self.wfile.write(body)
            return
            
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