"""Simple HTML pages."""
from flask import Blueprint, render_template, render_template_string, request

bp = Blueprint("pages", __name__)


@bp.get("/")
def index():
    return render_template("index.html", name=request.args.get("name", "guest"))


@bp.get("/greet")
def greet():
    name = request.args.get("name", "guest")
    return render_template_string(f"<h1>Hello {name}!</h1>")
