#!/usr/bin/node
/* exports to make it visable outside */
exports.addMeMaybe = function (x, theFunction) {
  theFunction(++x);
};
