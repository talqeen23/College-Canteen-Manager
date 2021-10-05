# -*- coding: utf-8 -*-
__version__ = '0.1'
from flask import Flask


app = Flask('pitho')
app.config['SECRET_KEY'] = 'randomkey'
app.debug = True
app.config['base_theme']=''
from pitho.controllers.user import *
from pitho.controllers.author import *
from pitho.controllers.admin import *

