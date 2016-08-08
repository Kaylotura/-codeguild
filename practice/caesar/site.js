'use strict';
/**
 * One function converts a string into a ceaser cipher based on a key,
 * the other returns a translated string based on a decipher key.
 *
 * Cipher example: 'cats', 1 -> 'dbut'
 * Decipher example:  fqiu', 2 -> 'dogs'
 */


var ALPHA_TO_NUMBER = 'abcdefghijklmnopqrstuvwxyz'.split('');
/** Takes in a word and a key, and returns a caeser cypher version of
 * the word, if the word has any punctuation in it, the punctuation remains as
 * it was.
 *
 * It does this by assigning each letter an alphanumeric index, then
 * increasing that alphanumeric index by the value of the key, wrapping around
 * the alpbanumeric index. */
function encryptWord(plainString, key) {
  var cipher = '';
  var workingWord = _.toLower(plainString);
  for (var i = 0; i < workingWord.length; i += 1) {
    var workingLetter = workingWord.charAt(i);
    if (ALPHA_TO_NUMBER.indexOf(workingLetter) >= 0) {
      var oldAlphaIndex = ALPHA_TO_NUMBER.indexOf(workingLetter);
      if (key + oldAlphaIndex >= ALPHA_TO_NUMBER.length) {
        var newAlphaIndex = key + oldAlphaIndex - ALPHA_TO_NUMBER.length;
      } else {
        var newAlphaIndex = oldAlphaIndex + key;
      } cipher += ALPHA_TO_NUMBER[newAlphaIndex];
    } else {
      cipher += workingLetter;
    }
  } return cipher;
}

/** Takes in a group of words and a key, and returns a caeser cypher version of
 * string.*/
function caesarEncrypt(plainString, key) {
  var workingWords = plainString.split(' ');
  var cypheredSentence = [];
  for (var i = 0; i < workingWords.length; i += 1) {
    var cypheredWord = encryptWord(workingWords[i], key);
    cypheredSentence += cypheredWord + ' ';
  } return cypheredSentence;
}

/** Takes in a string in a caesar-cypher, and it's key, and returns the
 * decyphered string. */
function caesarDecrypt(plainString, key) {
  var backwardsKey = ALPHA_TO_NUMBER.length - key;
  var newString = plainString;
  return caesarEncrypt(newString, backwardsKey);
}


console.log('to sit in solemn silence in a dull, dark, dock (Cypher 7)');
console.log(caesarEncrypt('To sit in solemn silence in a dull, dark, dock', 7));
console.log('ur guehfgf uvf svfgf ntnvafg gur cbfgf! (Cypher 13)');
console.log(caesarDecrypt('ur guehfgf uvf svfgf ntnvafg gur cbfgf!', 13));
