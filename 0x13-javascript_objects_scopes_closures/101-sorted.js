#!/usr/bin/node

const myDict = require('./101-data').dict;

const newDict = {};
for (const key in myDict) {
  const newKey = myDict[key];
  if (newKey in newDict) {
    newDict[newKey].push(key);
  } else {
    const lista = [];
    lista.push(key);
    newDict[newKey] = lista;
  }
}
console.log(newDict);
