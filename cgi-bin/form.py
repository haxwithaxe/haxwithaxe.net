# -*- coding: utf-8 -*-
# vim: set noexpandtab tabstop=4 shiftwidth=4 :

import web
from web import form
import page

''' Form abstraction of web.py '''

class FormDef:

    items = []
    validators = []

    def __call__(self):
        return form.Form(*self.items, validators=self.validators)

    def textbox(self, id, desc=''):
        self.items.append(form.Textbox(id, description=desc))

    def password(self, id, vpass, desc='Password'):
        self.items.append(form.Password(id, vpass, description=desc))

    def button(self, type='submit', description='Submit'):
        self.items.append(form.Button(id, type=type, description=label))

    def validator(self, message, func):
        self.validators.append(form.Validator(message, func))


class Form(page.Page):
    ''' '''
    form = FormDef

    def on_GET(self):
        # do $:f.render() in the template
        if not form: raise ValueError('form attribute of Form instance must be set with an instance of web.form.Form')
        f = self.form()
        return self.render.register(f)

    def on_POST(self):
        f = self.form()
        if not f.validates():
            return render.register(f)
        else:
            return self.on_valid_form()

    def on_valid_form(self):
        pass


