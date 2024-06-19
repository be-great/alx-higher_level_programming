#!/usr/bin/node
/* exports to make it visable outside */
exports.callMeMoby = function (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};
