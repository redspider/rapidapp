# coding=utf-8

from __future__ import absolute_import

from {NAME} import app
from trex.flask import render_html
from flask import Blueprint, g, redirect, url_for, request, make_response
import os.path
from trex.support import ejson
import {NAME}.model as m
from datetime import datetime

blueprint = Blueprint('index', __name__)

@blueprint.route('/')
@render_html()
def index():
    return {}

app.register_blueprint(blueprint)
