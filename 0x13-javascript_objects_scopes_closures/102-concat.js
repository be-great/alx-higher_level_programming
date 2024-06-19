#!/usr/bin/node
const fs = require('fs');
const arg1 = process.argv[2];
const arg2 = process.argv[3];
const out = process.argv[4];
const f1 = fs.readFileSync(arg1).toString();
const f2 = fs.readFileSync(arg2).toString();
fs.writeFileSync(out, f1 + f2);
