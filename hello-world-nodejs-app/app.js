const express = require('express');
const app = express();
const PORT = 3000;

app.get('/', (req, res) => {
  res.send('Hello from inside my Docker container!');
});

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
