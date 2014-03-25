# -*- coding: utf-8 -*-
# vim: set noexpandtab tabstop=4 shiftwidth=4 :

import web
import config

''' Base class for web apps that abstract the web.py GET/POST methods. '''

class Page:
	''' Web page abstract class '''
	default_inputs = {'title':config.default_page_title}	# default values
	web_input = None	# class wide access to current web.input()
	render = web.template.render(config.templates_dir)	# class wide access to the template engine
	path = ''	# path given to the url variable
	render_on_get_return = True
        render_on_post_return = True

	def GET(self, *args):
		self.web_input = web.input()
		self.set_defaults()
		if self.render_on_get_return:
			return self.render.base(self.on_GET(), self.web_input)
		return self.on_GET()
	
        def POST(self, *args):
                self.web_input = web.input()
                self.set_defaults()
                if self.render_on_post_return:
                    return self.render.base(self.on_POST())
                return self.on_POST()

	def set_defaults(self):
		defaults = self.default_input.copy()	# avoid overwriting default_input
		# merge giving preference to web_input
		defaults.update(self.web_input)
		self.web_input = defaults

	def on_GET(self):
		''' example /placeholder '''
		if self.render:
			return self.render.index(self.web_input)
		else:
			return 'Hello world!'

        def on_POST(self):
                ''' example /placeholder '''
                if self.render:
                        return self.render.index(self.web_input)
                else:
                        return 'Hello world!'

