"""Extensions module. Each extension is initialized in the app factory
located in app.py.
"""
from flask_debugtoolbar import DebugToolbarExtension
from flask_wtf.csrf import CSRFProtect

csrf_protect = CSRFProtect()
debug_toolbar = DebugToolbarExtension()
