from __future__ import absolute_import

from trex.flask import Flask

app = Flask(__name__)



import trex.cdn
trex.cdn.FlaskCDN(app)

# Import these here to ensure that the app exists before all the code in the
# views/filters tries to execute
from . import view
