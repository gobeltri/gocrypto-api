import os
from flask import Flask

from coin import Coin

# Working both in C9 && Heroku
HOSTNAME = os.environ.get('IP', '0.0.0.0')
PORT = int(os.environ.get('PORT', '8080'))

# Flask app
app = Flask(__name__)

@app.route('/')
def root():
    content = '{"status":200}'
    return(build_json_response(content))
    
@app.route('/coins')
def coins():
    Coin.api_seed('COINMARKETCAP')
    content = Coin.get_json()
    return(build_json_response(content))


@app.route('/coin/<ticker>', methods=['GET', 'POST'])
def coin(ticker):
    Coin.api_seed('COINMARKETCAP')
    content = Coin.find_coin(ticker)
    return(build_json_response(content))


def build_json_response(content):
    response = app.make_response(content)
    response.headers['Content-Type'] = 'application/json'
    response.headers['Access-Control-Allow-Origin'] = '*'
    return(response)    

if __name__ == "__main__":
    app.run(host=HOSTNAME, port=PORT)
	
	