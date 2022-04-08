#!/usr/bin/node

const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  charPrint (c) {
    let pr = '';
    for (let x = 0; x < this.size; x++) {
      if (c) {
        pr = pr + c;
      } else {
        pr = pr + 'X';
      }
    }
    for (let y = 0; y < this.size; y++) {
      console.log(pr);
    }
  }
};
