#!/usr/bin/node

function add (a, b) {
  return a + b;
}

const numa = parseInt(process.argv[2]);
const numb = parseInt(process.argv[3]);
if (isNaN(numa) || isNaN(numb)) {
  console.log('NaN');
} else {
  console.log(add(numa, numb));
}
