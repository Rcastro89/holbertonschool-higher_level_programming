#!/usr/bin/node

const num = parseInt(process.argv[2]);
if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  for (let bucle = 0; bucle < num; bucle++) {
    console.log('C is fun');
  }
}
