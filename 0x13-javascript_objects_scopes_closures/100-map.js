#!/usr/bin/node
const list = require('./100-data.js').list;
/* create a new list */
console.log(list);
console.log(list.map((value, index) => value * index));
