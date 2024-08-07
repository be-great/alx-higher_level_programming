#!/usr/bin/node
// write a content into a file
const fs = require('fs');
const filepath = process.argv[2];
const content = process.argv[3];
fs.writeFile(filepath, content, (error) => {
  if (error) {
    console.error(error);
  }
});
