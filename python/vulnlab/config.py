"""Application settings."""
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "data", "vulnlab.db")
UPLOAD_DIR = os.path.join(BASE_DIR, "data", "uploads")

SECRET_KEY = "vulnlab-flask-session-key-2f9c1e7a"
PARTNER_API_TOKEN = "pk_live_vulnlab_9a8b7c6d5e4f3a2b1c0d9e8f7a6b5c4d"

# Read from the environment, with a default.
LOG_LEVEL = os.environ.get("VULNLAB_LOG_LEVEL", "INFO")
