#!/usr/bin/node
// write a content into a file
const fs = require('fs');
const filepath = process.argv[2];
const content = process.argv[3];
function writeFile (filepath) {
  fs.writeFile(filepath, content, 'utf8', (err) => {
    if (err) {
      console.error(err);
    }
  });
}

if (filepath && content) {
  writeFile(filepath, content);
}
