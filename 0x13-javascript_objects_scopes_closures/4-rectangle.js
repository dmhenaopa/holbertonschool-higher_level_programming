#!/usr/bin/node
// A class Rectangle with 3 methods print(), rotate() and double()
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let row = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        row += 'X';
      }
      console.log(row);
      row = '';
    }
  }

  rotate () {
    const temporal = this.width;
    this.width = this.height;
    this.height = temporal;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}

module.exports = Rectangle;
