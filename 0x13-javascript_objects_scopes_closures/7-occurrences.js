#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  const listaTotal = list.filter(element => element === searchElement);
  return listaTotal.length;
};
