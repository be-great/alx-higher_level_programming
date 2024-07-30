#!/usr/bin/node
// prints all characters of a Star wars
const request = require('request');
const movieID = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/';
function printCharacters(movieID) {
    const fullurl = `${url}${movieID}/`;
    request.get(fullurl, { json: true}, (error, response, body) => {
        if (response.statusCode == 200) {
            if (body.characters && body.characters.length > 0 ) {
                body.characters.forEach(characterUrl  => {
                    request.get(characterUrl, { json: true}, (err0, repos0, body0) => {
                        if (repos0.statusCode == 200) {
                            console.log(body0.name);
                        }
                    });
                });
            }
        }
    });
}

if (movieID) {
    printCharacters(movieID);
}