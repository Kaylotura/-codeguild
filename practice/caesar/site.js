'use strict';
/**
 * One function converts a string into a ceaser cipher based on a key,
 * the other returns a translated string based on a decipher key.
 *
 * Cipher example: 'cats', 1 -> 'dbut'
 * Decipher example:  fqiu', 2 -> 'dogs'
 */

var ALPHA_TO_NUMBER = 'abcdefghijklmnopqrstuvwxyz'.split('');

/** Takes in a letter and a key, and returns a caeser cypher version of
string. It does this by assigning each letter an alphanumeric index, then
increasing that alphanumeric index by the value of the key, wrapping around
the alpbanumeric index. */
// var plainStringLetters = plainString.split('');


// function caesarEncrypt(plainString, key) {
//   var cipher = [];
//   for (var i = 0; i < plainString.length; i += 1) {
//     var workingString = _.toLower(plainString);
//     var workingLetter = workingString.charAt(i);
//     var oldAlphaIndex = ALPHA_TO_NUMBER.indexOf(workingLetter);
//     if (key + oldAlphaIndex >= ALPHA_TO_NUMBER.length) {
//       var newAlphaIndex = key + oldAlphaIndex - ALPHA_TO_NUMBER.length;
//     } else {
//       var newAlphaIndex = oldAlphaIndex + key;
//     } cipher += ALPHA_TO_NUMBER[newAlphaIndex];
//   } return cipher;
// }

function caesarEncrypt(plainString, key) {
  var lowersString = _.toLower(plainString);
  var workingLetters = lowersString.split('');
  var cipher = _.reduce(workingLetters, function(letter) {
    var oldAlphaIndex = ALPHA_TO_NUMBER.indexOf(letter);
    if (key + oldAlphaIndex >= ALPHA_TO_NUMBER.length) {
      var newAlphaIndex = key + oldAlphaIndex - ALPHA_TO_NUMBER.length;
    } else {
      var newAlphaIndex = oldAlphaIndex + key;
    } return ALPHA_TO_NUMBER[newAlphaIndex];
  });
  return cipher;
}



/** Takes in a string in a caesar-cypher, and it's key, and returns the
decyphered string. */
function caesarDecrypt(plainString, key) {
  var backwardsKey = ALPHA_TO_NUMBER.length - key;
  var newString = plainString;
  return caesarEncrypt(newString, backwardsKey);
}

console.log(caesarEncrypt('bat', 12));
console.log(caesarDecrypt('nmf', 12));
