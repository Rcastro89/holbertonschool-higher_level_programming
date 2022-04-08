#!/usr/bin/node

const myList = require('./100-data').list;

const newList = myList.map(num => num * myList.indexOf(num));
console.log(myList);
console.log(newList);
