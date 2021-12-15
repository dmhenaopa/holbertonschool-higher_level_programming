#!/usr/bin/node
// Class Square that inherits from Square
const Parent = require('./5-square');

class Square extends Parent {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }

    let row = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        row += c;
      }
      console.log(row);
      row = '';
    }
  }
}

module.exports = Square;
