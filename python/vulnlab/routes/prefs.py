"""User display preferences stored in a cookie."""
import base64
import pickle

from flask import Blueprint, make_response, request

bp = Blueprint("prefs", __name__, url_prefix="/prefs")

DEFAULT_PREFS = {"theme": "light", "page_size": 20}


@bp.get("/")
def get_prefs():
    raw = request.cookies.get("prefs")
    if not raw:
        return DEFAULT_PREFS
    return pickle.loads(base64.b64decode(raw))


@bp.post("/")
def set_prefs():
    prefs = {**DEFAULT_PREFS, **(request.get_json(force=True) or {})}
    resp = make_response(prefs)
    resp.set_cookie("prefs", base64.b64encode(pickle.dumps(prefs)).decode())
    return resp
