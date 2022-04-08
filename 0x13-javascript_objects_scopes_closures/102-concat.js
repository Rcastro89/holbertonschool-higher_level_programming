#!/usr/bin/node

const fs = require('fs');
const arch1 = fs.readFileSync(process.argv[2], 'utf8');
const arch2 = fs.readFileSync(process.argv[3], 'utf8');
fs.appendFileSync(process.argv[4], arch1 + '\n' + arch2 + '\n', 'utf8');
