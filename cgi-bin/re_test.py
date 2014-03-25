# -*- coding: utf-8 -*-
# vim: set noexpandtab tabstop=4 shiftwidth=4 :

import re
import web
import form

class RETest(form.Form):
    path = 're_test'
    def __init__(self):
        self.form.textbox('regex', 'Regex (Python):')
        self.form.textbox('input', 'Input Text:</label>')
        self.form.button('submit','Submit')

    def on_valid_form(self):
        regex = self.web_input.regex
        user_input = self.web_input.input
        if regex and user_input:
            result = re.findall(regex, user_input)
            if result:
                result = ', '.join(result)
        return result

