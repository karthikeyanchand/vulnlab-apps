const express = require("express");
const jwt = require("jsonwebtoken");
const { JWT_SECRET } = require("../config");

const router = express.Router();

router.post("/login", (req, res) => {
  const { username } = req.body || {};
  if (!username) return res.status(400).json({ error: "username required" });
  const token = jwt.sign({ sub: username }, JWT_SECRET, { expiresIn: "1h" });
  res.json({ token });
});

router.get("/continue", (req, res) => {
  res.redirect(req.query.next || "/");
});

module.exports = router;
