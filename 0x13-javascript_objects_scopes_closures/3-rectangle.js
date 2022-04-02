#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    this.width = w;
    this.height = h;
  }

  print() {
    for (i=0; i<this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
};
