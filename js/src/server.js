// VulnLab (JS) - a deliberately vulnerable Express app for security training.
// DO NOT deploy this anywhere. It binds to 127.0.0.1 only.
const express = require("express");
const { PORT } = require("./config");

const app = express();
app.use(express.json());

app.use("/users", require("./routes/users"));
app.use("/tools", require("./routes/tools"));
app.use("/files", require("./routes/files"));
app.use("/settings", require("./routes/settings"));
app.use("/search", require("./routes/search"));
app.use("/integrations", require("./routes/integrations"));
app.use("/calc", require("./routes/calc"));
app.use("/auth", require("./routes/auth"));

app.get("/health", (_req, res) => res.json({ status: "ok" }));

if (require.main === module) {
  app.listen(PORT, "127.0.0.1", () => {
    console.log(`VulnLab JS listening on http://127.0.0.1:${PORT}`);
  });
}

module.exports = app;
