#!/usr/bin/node

const request = require('request');
let personajesOrdenados = [];
let personajes = [];

function buscar() {
    try {
        const url = 'https://swapi-api.hbtn.io/api/films';
        request(url, (error, response, body) => {
            if (error) throw error;
            const obj = JSON.parse(body);
            const cantPersonajes = (obj.results[process.argv[2] - 1].characters).length;
            personajesOrdenados = Object.assign([], obj.results[process.argv[2] - 1].characters);
            console.log(personajesOrdenados);
            for (let x = 0; x < cantPersonajes; x++) {
                const url1 = personajesOrdenados[x];
                const d = request(url1, (error1, response1, body1) => {
                    const obj1 = JSON.parse(body1);
                    const nombre = obj1.name;
                    personajes[url1] = nombre;
                });
            }
        });
    } catch (error) {
        console.log(error);
    }
}

buscar();
console.log(personajes);