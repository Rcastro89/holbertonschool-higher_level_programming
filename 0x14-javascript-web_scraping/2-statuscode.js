#!/usr/bin/node

const request = require('request');

try {
  const url = process.argv[2];
  request(url, (error, response, body) => {
    try {
      if (error) throw error;
      console.log('code:', response.statusCode);
    } catch (err) {
      console.log(err);
    }
  });
} catch (err) {
  console.log(err);
}
