#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w && h && w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let pr = '';
    for (let x = 0; x < this.width; x++) {
      pr = pr + 'X';
    }
    for (let y = 0; y < this.height; y++) {
      console.log(pr);
    }
  }

  rotate () {
    const w = this.width;
    this.width = this.height;
    this.height = w;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};
