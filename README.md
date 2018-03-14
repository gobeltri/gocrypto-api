# gocrypto-fees
Comparing withdraw fees from different crypto exchanges.

## Live API
https://gocrypto-fees.herokuapp.com/api/v1

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
git clone https://github.com/gobeltri/gocrypto-fees.git
cd gocrypto-fees
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
