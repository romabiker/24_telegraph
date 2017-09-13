from flask_debugtoolbar import DebugToolbarExtension
from flask_wtf.csrf import CSRFProtect


csrf_protect = CSRFProtect()
debug_toolbar = DebugToolbarExtension()
