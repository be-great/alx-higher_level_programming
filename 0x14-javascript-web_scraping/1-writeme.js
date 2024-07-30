#!/usr/bin/node
// write a content into a file
const fs = require('fs');
const filepath = process.argv[2];
const content = process.argv[3];
function write (filepath, content) {
  fs.writeFile(filepath, content, (err) => {
    if (err) {
      console.error(err);
    }
  });
}

if (filepath && content) {
  write(filepath, content);
}
