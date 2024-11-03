from .api import api_bp
from .views import views_bp

def register_blueprints(app):
    app.register_blueprint(api_bp, url_prefix="/api")
    app.register_blueprint(views_bp)