#!/usr/bin/python

import os
import sys
import BaseHTTPServer, SimpleHTTPServer
import ssl

host = 'localhost'
port = 8443

httpd = BaseHTTPServer.HTTPServer((host, port), SimpleHTTPServer.SimpleHTTPRequestHandler)
httpd.server_forever()


