from http.server import HTTPServer, SimpleHTTPRequestHandler
import time
import json
import os
from gocrypto_fees import build_fees_list
from coin import Coin


# Working both in C9 && Heroku
HOSTNAME = os.environ.get('IP', '0.0.0.0')
PORT = int(os.environ.get('PORT', '8080'))
API_PATH = '/api/v1'


# Override SimpleHTTPRequestHandler to serve GET requests
class MyRequestHandler(SimpleHTTPRequestHandler):
    
    def do_GET(self):
        
        # Root path
        if self.path == '/':
            self.path = '/public/index.html'
            return SimpleHTTPRequestHandler.do_GET(self)
        
        # API path
        elif self.path == API_PATH:
            
            # Response ok
            self.send_response(200)
        
            # JSON Header
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
        
            # Print coin list in JSON format
            Coin.api_seed('COINMARKETCAP')
            content = Coin.get_json()
            body = content.encode('UTF-8', 'replace')
            self.wfile.write(body)
            
            
            
            
        # Other paths > call super class
        else:
            return SimpleHTTPRequestHandler.do_GET(self)

def run_goserver(hostname, port):
    httpd = HTTPServer((hostname, port), MyRequestHandler)
    print(time.asctime(), "Server Starts - %s:%s" % (hostname, port))

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print(time.asctime(), "Server Stops - %s:%s" % (hostname, port))


if __name__ == "__main__":
	run_goserver(HOSTNAME, PORT)