const express = require("express");
const { deepMerge } = require("../lib/merge");

const router = express.Router();
const settings = { theme: "light", notifications: { email: true } };

router.get("/", (_req, res) => res.json(settings));

router.patch("/", (req, res) => {
  deepMerge(settings, req.body || {});
  res.json(settings);
});

module.exports = router;
