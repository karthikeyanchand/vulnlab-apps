const fs = require("node:fs");
const path = require("node:path");
const crypto = require("node:crypto");
const { DatabaseSync } = require("node:sqlite");
const { DB_PATH, UPLOAD_DIR } = require("./config");

fs.mkdirSync(path.dirname(DB_PATH), { recursive: true });
fs.mkdirSync(UPLOAD_DIR, { recursive: true });

const db = new DatabaseSync(DB_PATH);

db.exec(`CREATE TABLE IF NOT EXISTS users (
  id INTEGER PRIMARY KEY,
  username TEXT UNIQUE,
  email TEXT,
  role TEXT,
  password_hash TEXT
)`);

const seed = db.prepare(
  "INSERT OR IGNORE INTO users (username, email, role, password_hash) VALUES (?, ?, ?, ?)"
);
const hash = crypto.createHash("sha256").update("changeme").digest("hex");
for (const [u, e, r] of [
  ["alice", "alice@example.test", "admin"],
  ["bob", "bob@example.test", "member"],
  ["carol", "carol@example.test", "member"],
]) {
  seed.run(u, e, r, hash);
}

module.exports = db;
