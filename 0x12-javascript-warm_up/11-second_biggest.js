#!/usr/bin/node

if (process.argv.length <= 2) {
  console.log(0);
} else if (process.argv.length === 3) {
  console.log(0);
} else {
  let arreglo = [];
  let vueltas = 0;
  process.argv.forEach(function (elemento) {
    if (vueltas > 1) {
      arreglo[arreglo.length] = parseInt(elemento);
    }
    vueltas++;
  });
  arreglo = arreglo.filter(function (maximo) {
    return maximo !== Math.max(...arreglo);
  });
  console.log(Math.max(...arreglo));
}
