#!/usr/bin/node

const num = parseInt(process.argv[2]);
let impresion = '';
if (isNaN(num)) {
  console.log('Missing size');
} else {
  for (let linea = 0; linea < num; linea++) {
    impresion = impresion + 'X';
  }
  for (let colum = 0; colum < num; colum++) {
    console.log(impresion);
  }
}
