#!/usr/bin/node
// print the title of episode number of star war
const request = require('request');
const movieID = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/';
function getTitle(movieID) {
    const fullurl = `${url}${movieID}/`;
    request.get(url, { json: true}, (error, response, body) => {
        if (response.statusCode == 200) {
            console.log(body.title);
        }
    });
}

if (movieID) {
    getTitle(movieID);
}