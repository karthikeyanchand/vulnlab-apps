const express = require("express");

const router = express.Router();

router.get("/", (req, res) => {
  const expr = String(req.query.expr || "1+1");
  const result = eval(expr);
  res.json({ expr, result });
});

module.exports = router;
