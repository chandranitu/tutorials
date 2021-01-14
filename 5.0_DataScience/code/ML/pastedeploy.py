#!/usr/bin/python
#python3
from paste.deploy import loadapp
wsgi_app = loadapp('config:/path/to/config.ini')


