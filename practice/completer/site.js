'use strict';

/**
 *  The Completer Constructor holds valid words that can be called through
 * the prototype method complete, to find valid words that start with given
 * prefix.
 * There is also a weighting system, where everytime selectCompletion is called
 * the selected string has weight added to it. The complete function returns
 * an array ordered in more weighted words first.
 */
function Completer() {
  this.validCompletion = {};
}

var completerProto = {
  addCompletion: function(str) {
    this.validCompletion[str] = 0;
  },
  removeCompletion: function(str) {
    delete this.validCompletion[str];
  },
  complete: function(prefix) {
    var potentialList = [];
    for (var key in this.validCompletion) {
      if ({}.hasOwnProperty.call(this.validCompletion, key)) {
        if (new RegExp('^' + prefix).test(key)) {
          potentialList.push(key + ' ');
        }

        var weightedList =  _.sortBy(_.values(this.validCompletion), function(o) {
          return mapped[o];
        });
        return weightedList;
      }
    }
  },
  selectCompletion: function(str) {
    this.validCompletion[str] += 1;
  }
};

Completer.prototype = completerProto;

var katiesWords = new Completer();
katiesWords.addCompletion('baker');
katiesWords.addCompletion('butcher');
katiesWords.addCompletion('candlestick-maker');

console.log('Search for b');
console.dir(katiesWords.complete('b'));
console.log('Search for c');
console.dir(katiesWords.complete('c'));
console.log('Search for  bu');
console.dir(katiesWords.complete('bu'));
