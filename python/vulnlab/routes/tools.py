"""Network diagnostic helpers for the ops dashboard."""
import subprocess

from flask import Blueprint, request

bp = Blueprint("tools", __name__, url_prefix="/tools")


@bp.get("/ping")
def ping():
    host = request.args.get("host", "127.0.0.1")
    out = subprocess.run(
        f"ping -c 1 {host}", shell=True, capture_output=True, text=True, timeout=5
    )
    return {"output": out.stdout}


@bp.get("/lookup")
def lookup():
    host = request.args.get("host", "localhost")
    out = subprocess.run(
        ["nslookup", host], capture_output=True, text=True, timeout=5
    )
    return {"output": out.stdout}
