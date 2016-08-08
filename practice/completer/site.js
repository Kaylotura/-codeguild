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
      if (prefix.test(word)) {
        potentialList += word + ' ';
      }
    }
  }
};

Completer.prototype = completerProto;

var katiesWords = new Completer();
katiesWords.addCompletion('baker');
katiesWords.addCompletion('butcher');
katiesWords.addCompletion('candlestick-maker');
