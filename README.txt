# Python Flask Server

## Overview
This server was developed using python-flask. Python-flask is a web application framework written in Python.
The REST APIs were edited online with a Swagger editor.

This application uses the [Connexion](https://github.com/zalando/connexion) library on top of Flask.

## Requirements
Python 3.5.2+

## Usage
To run the server, please execute the following from the root directory:

```
pip3 install -r requirements.txt
python main.py
```

and open your browser to here:

```
http://localhost:8080//ui/
```

Your Swagger definition lives here:

```
http://localhost:8080//swagger.json
```

To launch the integration tests, use pytest:
```
pip install pytest
python -m pytest
```
