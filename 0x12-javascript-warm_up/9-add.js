#!/usr/bin/node
function add (a, b) {
  const res = a + b;
  console.log(res);
}
add(Number(process.argv[2]), Number(process.argv[3]));
