#!/usr/bin/node

const fs = require('fs');

try {
  const leer = fs.readFileSync(process.argv[2], 'utf-8');
  console.log(leer);
} catch (err) {
  console.log(err);
}
