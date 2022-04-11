#!/usr/bin/node

const request = require('request');

let cuenta = 0;
try {
  const url = process.argv[2];
  request(url, (error, response, body) => {
    if (error) throw error;
    const obj = JSON.parse(body);
    for (let x = 0; x <= ((obj.results).length) - 1; x++) {
      for (let y = 0; y <= ((obj.results[x].characters).length) - 1; y++) {
        const validar = (obj.results[x].characters[y]).indexOf('18');
        if (validar !== -1) {
          cuenta++;
        }
      }
    }
    console.log(cuenta);
  });
} catch (error) {
  console.log(error);
}
