#!/usr/bin/node
// read and print the content of a file
const fs = require('fs')
const filepath = process.argv[2];
function readFile(filepath) {
    fs.readFile(filepath, 'utf8', (err, data) => {
        if (err) {
            console.error(err);
        } else {
            console.log(data);
        }
    });
}

if (filepath) {
    readFile(filepath);
}
