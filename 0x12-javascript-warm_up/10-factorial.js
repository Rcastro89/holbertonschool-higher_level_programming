#!/usr/bin/node

function factorial (numero) {
  numero = Math.abs(numero);
  if (numero <= 1) return 1;
  return numero * factorial(numero - 1);
}

const numero = parseInt(process.argv[2]);
if (isNaN(numero)) {
  console.log(1);
} else {
  console.log(factorial(numero));
}
