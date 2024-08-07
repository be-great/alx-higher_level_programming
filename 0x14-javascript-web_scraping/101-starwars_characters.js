#!/usr/bin/node
// print all characters of a star war movie
// same order of the list “characters”
const request = require('request');
const movieID = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/';
function printCharacters (movieID) {
  const fullurl = `${url}${movieID}/`;
  request.get(fullurl, { json: true }, (error, response, body) => {
    if (error) {
      console.log(error);
    } else if (response.statusCode === 200) {
      const characterUrls = body.characters;
      if (characterUrls.length === 0) {
        return;
      }
      function fetchCharacter (index) {
        if (index >= characterUrls.length) { return; }
        const characterUrl = characterUrls[index];
        request.get(characterUrl, { json: true }, (err0, repos0, body0) => {
          if (err0) {
            console.log(err0);
          } else if (repos0.statusCode === 200) {
            console.log(body0.name);
            fetchCharacter(index + 1);
          }
        });
      }
      fetchCharacter(0);
    }
  });
}

if (movieID) {
  printCharacters(movieID);
}
