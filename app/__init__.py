import os
from flask import Flask, render_template, current_app, session, redirect, url_for
from config import active_config
from app.extensions import db
from app.models import User # Ensure models are loaded

def create_app(config_class=active_config):

    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Configure Uploads
    app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'static', 'uploads')
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])

    # Initialize Flask extensions
    db.init_app(app)
    from flask_wtf.csrf import CSRFProtect
    CSRFProtect(app)

    # Register Blueprints
    from app.routes.main import main_bp
    from app.routes.auth import auth_bp
    from app.routes.admin import admin_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(admin_bp)

    # Global Error Handlers
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('errors/404.html'), 404

    @app.errorhandler(500)
    def internal_server_error(e):
        app.logger.error(f"Internal Server Error: {str(e)}")
        # In production, we don't expose any details
        return render_template('errors/500.html'), 500

    @app.before_request
    def force_admin_safe():
        # This hook runs before every request.
        # We ensure that if anything fails here, we handle it gracefully.
        try:
            # Placeholder for any global pre-flight checks (e.g. DB heartbeat)
            pass
        except Exception:
            app.logger.error("Global before_request failure")
            return redirect(url_for('main.index'))

    return app


