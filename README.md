# Python REST API Tutorial

### Requirements
- Python
- Flask
- Flask-SQLAlchemy
- Flask-REstful
- SQLite3
- Jsonify

### Dev Environment Setup
We can create a ```virtualenv``` first so the packages don't mess with your python installation.

Make sure you have ```virtualenv``` installed. You can, however, skip this part and jump dirctly
to the ```pip``` installation.

```
$ virtualenv venv
$ source venv/bin/activate
$ pip install flask flask-jsonpify flask-sqlalchemy flask-restful
$ pip freeze
```

### Run The app

Now you can clone the repo, and execute ```python server.py``` to run the server.
