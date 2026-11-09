const express = require("express");
const path = require("node:path");
const { UPLOAD_DIR } = require("../config");

const router = express.Router();

router.get("/download", (req, res) => {
  const name = req.query.name || "";
  res.sendFile(path.join(UPLOAD_DIR, name));
});

router.get("/thumbnail", (req, res) => {
  const name = path.basename(String(req.query.name || ""));
  const full = path.resolve(UPLOAD_DIR, name);
  if (!full.startsWith(UPLOAD_DIR + path.sep)) return res.status(400).end();
  res.sendFile(full);
});

module.exports = router;
