"""Tiny SQLite helper with seed data."""
import hashlib
import os
import sqlite3

from . import config

SEED_USERS = [
    ("alice", "alice@example.test", "admin"),
    ("bob", "bob@example.test", "member"),
    ("carol", "carol@example.test", "member"),
]


def get_conn() -> sqlite3.Connection:
    conn = sqlite3.connect(config.DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db() -> None:
    os.makedirs(os.path.dirname(config.DB_PATH), exist_ok=True)
    os.makedirs(config.UPLOAD_DIR, exist_ok=True)
    with get_conn() as conn:
        conn.execute(
            "CREATE TABLE IF NOT EXISTS users ("
            "id INTEGER PRIMARY KEY, username TEXT UNIQUE, email TEXT, "
            "role TEXT, password_hash TEXT)"
        )
        for username, email, role in SEED_USERS:
            conn.execute(
                "INSERT OR IGNORE INTO users (username, email, role, password_hash) "
                "VALUES (?, ?, ?, ?)",
                (username, email, role, hashlib.sha256(b"changeme").hexdigest()),
            )
