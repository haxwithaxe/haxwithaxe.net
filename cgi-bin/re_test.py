#!/usr/bin/env python

import re
import cgi

print('Content-type: text/html\n\n')
result = ''
form = '''<form target="re_test.py" method="post">
	<label>Regex (Python):</label>
	<input type="text" name="regex" /><br/>
	<label>Input Text:</label>
	<input type="text" name="input" /><br/>
	<input type="submit">
	</form>'''

page = '''<html><body>%s</br><label>Result:</label></br>%s</body></html>'''

vals = cgi.FieldStorage()
if vals.has_key('regex') and vals.has_key('input'):
	regex = vals.getvalue('regex')
	user_input = vals.getvalue('input')
	if regex and user_input and len(regex) > 0 and len(user_input) > 0:
		result = re.findall(regex,user_input)
		if result: result = ', '.join(result)

print(page % (form,result))	


