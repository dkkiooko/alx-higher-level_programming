#!/usr/bin/node
// class that defines a rectangle

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  // method to print a rectangle image with "X"
  print () {
    let line;
    for (let i = 0; i < this.height; i++) {
      line = 'X';
      for (let j = 0; j < this.width - 1; j++) {
        line += 'X';
      }
      console.log(line);
    }
  }

  // method that exchanges the width and the height of the rectangle
  rotate () {
    const a = this.width;
    this.width = this.height;
    this.height = a;
  }

  // method that doubles the dimensions of the rectangle
  double () {
    this.width = this;
  }
}
module.exports = Rectangle;
