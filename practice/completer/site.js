'use strict';

/**
 * The Completer Constructor holds valid words that can be called through
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
  /**
   * The Add Completion prototype method takes in a string and adds it as a
   * valid entry into the validCompletionToWeight object, and sets its weight
   * to zero.
   */
  addCompletion: function(str) {
    this.validCompletionToWeight[str] = 0;
  },
  /**
   * The Remove Completion prototype method takes in a string, and deletes it
   * from the validCompletionToWeight object.
   */
  removeCompletion: function(str) {
    delete this.validCompletionToWeight[str];
  },
  /**
   * The Complete prototype method takes in a string, converts it into a prefix
   * reglar expression, and iterates through the validCompletionToWeight object
   * seeking a match based on the first part of the strings within
   * validCompletionToWeight. It then returns the matches ordered by their
   * weight.
   */
  complete: function(prefix) {
    var potentialWords = _.filter(
      _.keys(this.validCompletionToWeight), function(o) {
        return new RegExp('^' + prefix).test(o);
      });
    var weightedList =  _.sortBy(potentialWords).reverse();
    return weightedList;
  },
  /**
   * The Select Completion prototype method simply adds one to the weight value
   * for the given string key in validCompletionToWeight.
   */
  selectCompletion: function(str) {
    this.validCompletionToWeight[str] += 1;
  }
};

Completer.prototype = completerProto;


/**
 * A series of console tests.
 */
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
