#!/usr/bin/node
//  gets the contents of a webpage and stores it in a file.
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filepath = process.argv[3];
function getContent (url, filepath) {
  request.get(url, (error, response, body) => {
    if (error) {
      console.log(error);
    } else if (response.statusCode === 200) {
      fs.writeFile(filepath, body, 'utf8', (err) => {
        if (err) {
          console.error(err);
        }
      });
    }
  });
}

if (url && filepath) {
  getContent(url, filepath);
}
