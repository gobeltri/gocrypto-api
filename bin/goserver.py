import os
from flask import Flask

from coin import Coin


# Working both in C9 && Heroku
HOSTNAME = os.environ.get('IP', '0.0.0.0')
PORT = int(os.environ.get('PORT', '8080'))
API_PATH = '/api/v1'

# Flask app
app = Flask(__name__)
    
@app.route(API_PATH)
def api():
    # Print coin list in JSON format
    Coin.api_seed('COINMARKETCAP')
    content = Coin.get_json()
    body = content.encode('UTF-8', 'replace')
    
    response = app.make_response(body)
    response.headers['Content-Type'] = 'application/json'
    response.headers['Access-Control-Allow-Origin'] = '*'
    return(response)
    
if __name__ == "__main__":
    app.run(host=HOSTNAME, port=PORT)
	
	