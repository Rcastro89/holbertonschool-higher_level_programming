#!/usr/bin/node

const request = require("request");

try {
    var url = process.argv[2];
    request(url, (error, response, body) => {
        try {
            console.log("code:", response.statusCode);
        } catch (err) {
            console.log(err);
        }
    });
} catch (err) {
    console.log(err);
}