#!/usr/bin/node
const dict = require('./101-data').dict;
const res = {};
for (const id in dict) {
  const occr = dict[id];
  /* push to existing array or create new */
  if (res[occr]) {
    res[occr].push(id.toString());
  } else {
    res[occr] = [id.toString()];
  }
}
console.log(res);
