#!/usr/bin/node

const arreglo = [];

exports.logMe = function (item) {
  arreglo.push(item);
  const total = arreglo.length - 1;
  console.log(total + ': ' + arreglo[total]);
};
