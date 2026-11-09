"""User directory endpoints."""
from flask import Blueprint, abort, jsonify, request

from ..db import get_conn
from ..services.passwords import hash_password

bp = Blueprint("users", __name__, url_prefix="/users")


@bp.get("/search")
def search_users():
    term = request.args.get("q", "")
    sql = f"SELECT id, username, email FROM users WHERE username LIKE '%{term}%'"
    with get_conn() as conn:
        rows = conn.execute(sql).fetchall()
    return jsonify([dict(r) for r in rows])


@bp.get("/<int:user_id>")
def get_user(user_id: int):
    with get_conn() as conn:
        row = conn.execute(
            "SELECT id, username, email FROM users WHERE id = ?", (user_id,)
        ).fetchone()
    if row is None:
        abort(404)
    return jsonify(dict(row))


@bp.post("/register")
def register():
    body = request.get_json(force=True)
    username, password = body["username"], body["password"]
    with get_conn() as conn:
        conn.execute(
            "INSERT INTO users (username, email, role, password_hash) VALUES (?, ?, 'member', ?)",
            (username, body.get("email", ""), hash_password(password)),
        )
    return {"created": username}, 201
