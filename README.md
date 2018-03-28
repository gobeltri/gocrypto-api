# Gocrypto
REST API with Crypto metrics.

## Use cases
* https://gocryp.github.io/
  * Compare crypto withdrawal fees.

## API
* https://gocrypto-api.herokuapp.com
* https://gocrypto-api.herokuapp.com/coins
* https://gocrypto-api.herokuapp.com/coin/\<ticker\>

## Development
Go to https://c9.io/new and create a new workspace from Python template.

```
# Get Python 3.6
sudo apt-get install python3.6
```

```
# Get Pipenv - Manages virtual environments from Pipfile (setuptools must be upgraded)
sudo python3 -m pip install --upgrade setuptools
sudo pip3 install pipenv
```

```
# Install virtual environment for current Pipfile and enter virtual shell
git clone https://github.com/gobeltri/gocrypto-api.git
cd gocrypto-api
pipenv install
pipenv shell
```

```
# Run server on https://<c9-workspace-name>-<c9-user-name>.c9users.io/api/v1
python bin/goserver.py 
```

## Deploy

### Heroku

```
wget -qO- https://cli-assets.heroku.com/install-ubuntu.sh | sh
heroku login
heroku git:remote -a <heroku-app-name>
```
