"""File upload/download endpoints."""
import os

from flask import Blueprint, current_app, request, send_file
from werkzeug.utils import secure_filename

bp = Blueprint("files", __name__, url_prefix="/files")


@bp.get("/download")
def download():
    name = request.args.get("name", "")
    path = os.path.join(current_app.config["UPLOAD_DIR"], name)
    return send_file(path)


@bp.post("/upload")
def upload():
    f = request.files["file"]
    safe_name = secure_filename(f.filename or "upload.bin")
    f.save(os.path.join(current_app.config["UPLOAD_DIR"], safe_name))
    return {"saved": safe_name}, 201
