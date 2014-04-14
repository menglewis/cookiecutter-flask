# -*- coding: utf-8 -*-
from flask import render_template

from . import public

@public.route('/', methods=['GET'])
def index():
    render_template('public/index.html')
