from flask import Flask, render_template


from telegraph import commands
from telegraph.extensions import csrf_protect, debug_toolbar
from telegraph.settings import ProdConfig
from .telegrams.views import telegrams_blueprint


def create_app(config_object=ProdConfig):
    app = Flask(
        __name__.split('.')[0],
        static_url_path='/static',
        static_folder='static_files',
    )
    app.config.from_object(config_object)
    register_extensions(app)
    register_blueprints(app)
    register_errorhandlers(app)
    register_commands(app)
    return app


def register_blueprints(app):
    app.register_blueprint(telegrams_blueprint)
    return None


def register_extensions(app):
    csrf_protect.init_app(app)
    debug_toolbar.init_app(app)
    return None


def register_errorhandlers(app):
    """Register error handlers."""
    def render_error(error):
        """Render error template."""
        # If a HTTPException, pull the `code` attribute; default to 500
        error_code = getattr(error, 'code', 500)
        return render_template('{0}.html'.format(error_code)), error_code
    for errcode in [401, 404, 500]:
        app.errorhandler(errcode)(render_error)
    return None


def register_commands(app):
    app.cli.add_command(commands.lint)
    app.cli.add_command(commands.clean)
    app.cli.add_command(commands.urls)
