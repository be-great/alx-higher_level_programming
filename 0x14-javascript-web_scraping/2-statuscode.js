#!/usr/bin/node
// display the status code of a "Get" request
const request = require('request');
const url = process.argv[2];
function getStatus(url) {
    request.get(url, (error, response) => {
        if (!error) {
            console.log(`code: ${response.statusCode}`)
        }
    });
}
if (url) {

}