const connectToMongo = require("./db");
const express = require("express");
var cors = require('cors');
const app = express();
const port = 8000;

app.use(cors()); 
app.use(express.json()); 

connectToMongo(); 

// Available Routes
app.use("/api/auth", require("./routes/auth"));
app.use('/api/scrape',require('./routes/scrape'));
app.use('/api/hatespeech',require('./routes/hatespeech'));

app.listen(port, () => {
  console.log(`cholebhatoore listening on port ${port}`);
});
