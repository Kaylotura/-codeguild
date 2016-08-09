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
  this.validCompletionToWeight = {};
}

var completerProto = {
  addCompletion: function(str) {
    this.validCompletionToWeight[str] = 0;
  },
  removeCompletion: function(str) {
    delete this.validCompletionToWeight[str];
  },
  complete: function(prefix) {
    var potentialWords = _.filter(
      _.keys(this.validCompletionToWeight), function(o) {
        return new RegExp('^' + prefix).test(o);
      });
    var weightedList =  _.sortBy(potentialWords, function(o) {
      return o;
    });
    return weightedList.reverse();
  },
  selectCompletion: function(str) {
    this.validCompletionToWeight[str] += 1;
  }
};

Completer.prototype = completerProto;

var katiesWords = new Completer();

katiesWords.addCompletion('bakre');
katiesWords.removeCompletion('bakre');
katiesWords.addCompletion('beekeeper');
katiesWords.addCompletion('baker');
katiesWords.addCompletion('butcher');
katiesWords.addCompletion('candlestick-maker');
katiesWords.selectCompletion('butcher');
katiesWords.selectCompletion('butcher');
katiesWords.selectCompletion('baker');

console.log('Search for b');
console.dir(katiesWords.complete('b'));
console.log('Search for c');
console.dir(katiesWords.complete('c'));
console.log('Search for  bu');
console.dir(katiesWords.complete('bu'));
