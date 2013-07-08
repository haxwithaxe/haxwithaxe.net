#!/usr/bin/env python

import cgi, os, sys

print('Content-Type: text/plain\n')
sys.stdout.write(os.environ['REMOTE_ADDR'])
