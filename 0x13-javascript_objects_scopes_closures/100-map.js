#!/usr/bin/node

const myList = require('./100-data').list;

let x = 0;
const newList = myList.map(num => num * x++);
console.log(myList);
console.log(newList);