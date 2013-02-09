from __future__ import absolute_import

from {NAME} import app
from flask import request, g, session, redirect, url_for
import {NAME}.model as m
from os import path
from glob import glob
from trex.support import browser

# Import all views
__all__ = [ path.basename(f)[:-3] for f in glob(path.dirname(__file__) + '/*.py') ]
from . import *

@app.before_request
def check_authentication(*args, **kwargs):
    if request.endpoint in ['static', 'cdn']:
        return

    g.user = None
