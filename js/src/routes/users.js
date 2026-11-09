const express = require("express");
const db = require("../db");

const router = express.Router();

router.get("/search", (req, res) => {
  const term = req.query.q || "";
  const rows = db
    .prepare(`SELECT id, username, email FROM users WHERE username LIKE '%${term}%'`)
    .all();
  res.json(rows);
});

router.get("/:id", (req, res) => {
  const row = db
    .prepare("SELECT id, username, email FROM users WHERE id = ?")
    .get(Number(req.params.id));
  if (!row) return res.status(404).end();
  res.json(row);
});

module.exports = router;
