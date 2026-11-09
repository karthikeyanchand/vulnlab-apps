const express = require("express");
const { exec, execFile } = require("node:child_process");

const router = express.Router();

router.get("/ping", (req, res) => {
  const host = req.query.host || "127.0.0.1";
  exec(`ping -c 1 ${host}`, { timeout: 5000 }, (err, stdout) => {
    res.json({ output: stdout, error: err ? err.message : null });
  });
});

router.get("/lookup", (req, res) => {
  const host = String(req.query.host || "localhost");
  execFile("nslookup", [host], { timeout: 5000 }, (err, stdout) => {
    res.json({ output: stdout, error: err ? err.message : null });
  });
});

module.exports = router;
