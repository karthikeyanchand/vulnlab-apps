"""VulnLab (Python) - a deliberately vulnerable Flask app for security training.

DO NOT deploy this anywhere. It binds to 127.0.0.1 only and exists so that
scanners and AI reviewers have known bugs to find.
"""
from flask import Flask

from . import config, db
from .routes import files, integrations, pages, prefs, tools, users


def create_app() -> Flask:
    app = Flask(__name__)
    app.config["SECRET_KEY"] = config.SECRET_KEY
    app.config["UPLOAD_DIR"] = config.UPLOAD_DIR

    db.init_db()

    for bp in (users.bp, files.bp, tools.bp, integrations.bp, prefs.bp, pages.bp):
        app.register_blueprint(bp)

    @app.get("/health")
    def health():
        return {"status": "ok"}

    return app
