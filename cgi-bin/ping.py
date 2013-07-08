#!/usr/bin/env python

import cgi
import cgitb; cgitb.enable()
import os

db_filename = '../ping.db'

form = cgi.FieldStorage()
host = form.getvalue('am',None)
pushed_ip = form.getvalue('ip',None)
remote_host = os.environ['REMOTE_ADDR']
record = '%s;%s;%s\n' % (host, pushed_ip, remote_host)
db = open(db_filename, 'a')
db.write(record)
db.close()
print('Content-Type: text/plain\n')
print(record)
