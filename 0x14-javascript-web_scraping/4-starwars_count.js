#!/usr/bin/node
// print the number of movie of a character present
// with id = 18
const request = require('request');
const url = process.argv[2];
const charId = 18;
function countMoviesWithCharacter (url, charId) {
  request.get(url, { json: true }, (error, response, body) => {
    if (error) {
      console.log(error);
    } else if (response.statusCode === 200) {
      const films = body.results;
      const count = films.filter(film => film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${charId}/`)).length;
      console.log(count);
    }
  });
}

if (url) {
  countMoviesWithCharacter(url, charId);
}
