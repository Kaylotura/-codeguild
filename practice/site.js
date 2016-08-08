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
    this.validcompletion.splice(this.validcompletion.indexOf('str'), 1);
  },
  complete: function(prefix) {
    // returns an array of all valid completions that start with the given prefix
  }
}
