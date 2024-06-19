#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
}
/* module.exports => object in nodejs to export the models */
/* to used on other files */
module.exports = Rectangle;
