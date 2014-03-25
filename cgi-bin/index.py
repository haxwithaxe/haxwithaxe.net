#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# vim: set noexpandtab tabstop=4 shiftwidth=4 :

import os
import web
import site
import config
import ping
import re_test
import whatismyip

home = '/cgi-bin/index'
os.environ["SCRIPT_NAME"] = home
os.environ["REAL_SCRIPT_NAME"] = home


my_pages = [ping.Ping, re_test.RETest, whatismyip.WhatIsMyIP]
my_site = site.Site(my_pages)

