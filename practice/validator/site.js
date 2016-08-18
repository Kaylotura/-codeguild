'use strict';

/**
 * The Validator takes in the user's input as they type into any given text box
 * in the form and uses kestroke events to visually que the user that their
 * input is either valid or not, by filling the field with a yellow background
 * while invalid.
 */

/**
 * Adds the invalid class to the given field (distinguished by a class).
 *
 * The invalid class has a yellow background in the site.css file.
 */
function makeFieldYellow(inputclass) {
  $('input.' + inputclass).addClass('invalid');
}

/**
 * Removes the invalid class from a given field (distinguished by a class).
 */
function removeYellowFromField(inputclass) {
  $('input.' + inputclass).removeClass('invalid');
}

/**
 * Takes in the name entry and returns a boolen representing whether or not the
 * entry is valid.
 */
function checkNameIfValid(nameEntry) {
  return /[a-z]+\s[a-z]+/i.test(nameEntry);
}

/**
* Takes in the birthday entry and returns a boolen representing whether or not
* the entry is valid.
 */
function checkBirthdayIfValid(birthdayEntry) {
  return /\d{4}\-(\d{2})\-(\d{2})/.test(birthdayEntry);
}

 /**
 * Takes in the phone number entry returns a boolen representing whether or not
 * the entry is valid.
  */
function checkPhoneNumberIfValid(phoneNumberEntry) {
  return /(\d{3})\-(\d{3})\-(\d{4})/.test(phoneNumberEntry);
}


/**
 *Retireves the entry from a given field, and returns it as a string.
 */
function getEntry(inputclass) {
  var entry = $('input.' + inputclass).prop('value');
  return entry;
}


/**
 * Takes in an inputclass, a boolean based on weather or not the entry
 * in that class is valid, and the entry itself, and toggles the invalid class
 * on the given inputclass field based on weather or not the entry is invalid,
 * or if it is empty.
 */
function toggleValidityClass(inputclass, bool, entry) {
  console.log(bool);
  if (bool) {
    removeYellowFromField(inputclass);
  } else {
    makeFieldYellow(inputclass);
  }
  if (!entry) {
    removeYellowFromField(inputclass);
  }
}


/**
 * Initiated by the event handler, this function grabs the entry for
 * fullname checks to see if it is valid, then runs the toggle validity
 * class function on the fullname field.'
 */
function runName() {
  var inputclass = 'fullname';
  var entry = getEntry(inputclass);
  var validityBoolean = checkNameIfValid(entry);
  toggleValidityClass(inputclass, validityBoolean, entry);
}

/**
 * Initiated by the event handler, this function grabs the entry for
 * birthday checks to see if it is valid, then runs the toggle validity
 * class function on the birthday field.'
 */
function runBirthday() {
  var inputclass = 'birthday';
  var entry = getEntry(inputclass);
  var validityBoolean = checkBirthdayIfValid(entry);
  toggleValidityClass(inputclass, validityBoolean, entry);
}

/**
 * Initiated by the event handler, this function grabs the entry for
 * phone-number checks to see if it is valid, then runs the toggle validity
 * class function on the phone number field.'
 */
function runPhoneNumber() {
  var inputclass = 'phone-number';
  var entry = getEntry(inputclass);
  var validityBoolean = checkPhoneNumberIfValid(entry);
  toggleValidityClass(inputclass, validityBoolean, entry);
}

/**
 * The event handler activates the corresponding run function based on the input
 * field that has just had a character entered after each keystroke.
 */
function registerEventHandlers() {
  $('.fullname').on('keyup', runName);
  $('.birthday').on('keyup', runBirthday);
  $('.phone-number').on('keyup', runPhoneNumber);
}

$(document).ready(registerEventHandlers);
