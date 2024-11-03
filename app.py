from flask import Flask
from config import Config
from extensions import db, ma
from routes import register_blueprints

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Laiendite algväärtustamine
    db.init_app(app)
    ma.init_app(app)

    # Loome andmebaasi ja lisame Blueprintid
    with app.app_context():
        db.create_all()
        register_blueprints(app)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
