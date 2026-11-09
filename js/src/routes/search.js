const express = require("express");
const _ = require("lodash");

const router = express.Router();

router.get("/", (req, res) => {
  const q = req.query.q || "";
  res.send(`<h1>Results for ${q}</h1><p>No results found.</p>`);
});

router.get("/safe", (req, res) => {
  const q = _.escape(String(req.query.q || ""));
  res.send(`<h1>Results for ${q}</h1><p>No results found.</p>`);
});

module.exports = router;
