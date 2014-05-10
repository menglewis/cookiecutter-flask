# -*- coding: utf-8 -*-
from flask import render_template

from . import main

@main.route('/', methods=['GET'])
def index():
    return render_template('main/index.html')