#!/usr/bin/node

const request = require('request');
try {
  const url = process.argv[2];
  request(url, (error, response, body) => {
    if (error) throw error;
    const myDict = {};
    const obj = JSON.parse(body);
    for (let x = 0; x <= obj.length - 1; x++) {
      if (obj[x].completed === true) {
        if (!myDict[obj[x].userId]) {
          myDict[obj[x].userId] = 1;
        } else {
          myDict[obj[x].userId]++;
        }
      }
    }
    console.log(myDict);
  });
} catch (err) {
  console.log(err);
}
