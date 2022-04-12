#!/usr/bin/node

const request = require('request');
const personajes = [];
try {
  const url = 'https://swapi-api.hbtn.io/api/films';
  request(url, (error, response, body) => {
    if (error) throw error;
    const obj = JSON.parse(body);
    const cantPersonajes = (obj.results[process.argv[2] - 1].characters).length;
    for (let x = 0; x < cantPersonajes; x++) {
      const url1 = obj.results[process.argv[2] - 1].characters[x];
      const d = request(url1, (error1, response1, body1) => {
        const obj1 = JSON.parse(body1);
        personajes.push(obj1.name);
        return obj1.name;
      });
    }
  });
} catch (error) {
  console.log(error);
}
