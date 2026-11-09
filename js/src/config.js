const path = require("node:path");

const ROOT = path.resolve(__dirname, "..");

module.exports = {
  DB_PATH: path.join(ROOT, "data", "vulnlab.db"),
  UPLOAD_DIR: path.join(ROOT, "data", "uploads"),
  JWT_SECRET: "vulnlab-jwt-signing-secret-7d1e9b3c5a",
  PORT: Number(process.env.PORT || 5002),
};
