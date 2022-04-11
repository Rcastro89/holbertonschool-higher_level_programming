#!/usr/bin/node

const fs = require('fs');

try {
  fs.writeFile(process.argv[2], process.argv[3], 'utf-8', (err) => {
    if (err) throw err;
  });
} catch (error) {
  console.log(error);
}
