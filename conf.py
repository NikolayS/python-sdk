# -*- coding: utf-8 -*-
# extensions = ['autoapi.extension']

def run_apidoc(_):
	from sphinx.apidoc import main
	import os
	import sys
	sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
	cur_dir = os.path.abspath(os.path.dirname(__file__))
	module = os.path.join(cur_dir, "..", "api")
	main(['-e', '-o', cur_dir, module, '--force'])

def setup(app):
	app.connect('builder-inited', run_apidoc)
