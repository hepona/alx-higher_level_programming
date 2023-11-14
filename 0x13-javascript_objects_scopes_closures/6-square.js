#!/usr/bin/node
const square = require('./5-square');
class Square extends square {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let cc = '';
      for (let j = 0; j < this.width; j++) {
        cc += c;
      }
      console.log(cc);
    }
  }
}
module.exports = Square;
