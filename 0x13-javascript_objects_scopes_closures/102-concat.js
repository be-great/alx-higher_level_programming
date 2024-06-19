#!/usr/bin/node
const fs = require('fs');
const f1 = fs.readFileSync(process.argv[2]).toString();
const f2 = fs.readFileSync(process.argv[3]).toString();
fs.writeFileSync(process.argv[4], f1 + f2);
