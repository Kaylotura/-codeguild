'use strict';

/**
 *  The Completer Constructor holds valid words that can be called through
 the prototype method complete, to find valid words that start with given prefix.
 */
function Completer() {
  this.validCompletion = [];
}

var completerProto = {
  addCompletion: function(str) {
    this.validCompletion.push(str);
  },
  removeCompletion: function(str) {
    this.validCompletion.splice(this.validCompletion.indexOf(str), 1);
  },
  complete: function(prefix) {
    var potentialList = [];
    for (var i = 0; i < this.validCompletion.length; i += 1) {
      var word = this.validCompletion[i];
      if (new RegExp('^' + prefix).test(word)) {
        potentialList.push(word + ' ');
      }
    } return potentialList;
  }
};

Completer.prototype = completerProto;

var katiesWords = new Completer();
katiesWords.addCompletion('bakre');
katiesWords.addCompletion('baker');
katiesWords.addCompletion('butcher');
katiesWords.addCompletion('candlestick-maker');
katiesWords.removeCompletion('bakre');

console.log('Search for b');
console.dir(katiesWords.complete('b'));
console.log('Search for c');
console.dir(katiesWords.complete('c'));
console.log('Search for  bu');
console.dir(katiesWords.complete('bu'));
