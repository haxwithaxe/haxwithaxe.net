# -*- coding: utf-8 -*-
# vim: set noexpandtab tabstop=4 shiftwidth=4 :

import web
import config
import page

class Ping(page.Page):
    path = 'ping'
    defaults = {'am':None, 'ip': None}

    def on_GET(self):
        remote_host = web.ctx.env.get('REMOTE_ADDR')
        record = '%s;%s;%s\n' % (host, pushed_ip, remote_host)
        db = open(config.ping_db_filename, 'a')
        db.write(record)
        db.close()
        return record
