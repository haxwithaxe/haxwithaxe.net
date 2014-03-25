# -*- coding: utf-8 -*-
# vim: set noexpandtab tabstop=4 shiftwidth=4 :

import web
import page

class WhatIsMyIP(page.Page):
    ''' '''
    page = 'whatismyip'
    def on_GET(self):
        return web.ctx.env.get('REMOTE_ADDR')
