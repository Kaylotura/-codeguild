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
 * Takes in a field (distinguished by a class) and the entry that has been
 * typed into the textbox of the given field, and returns a boolen representing
 * whether or not the entry is valid for the given field.
 */
function checkIfValid(inputclass, entry) {
  if (inputclass === 'fullname') {
    return /(\w+)\s(\w+)/.test(entry);
  } else if (inputclass === 'birthday') {
    return /(\d\d\d\d)\-(\d\d)\-(\d\d)/.test(entry);
  } else if (inputclass === 'phone-number') {
    return /(\d\d\d)\-(\d\d\d)\-(\d\d\d\d)/.test(entry);
  }
}


/**
 * Takes in an inputclass, determines it's current entry, checks to see if that
 * entry is valid, empty, or invalid. If it is valid or empty, it turns off the
 * yellow background, but if it is invalid, the background becomes yellow.
 */
function validateEntry(inputclass) {
  var entry = $('input.' + inputclass).prop('value');
  if (checkIfValid(inputclass, entry)) {
    removeYellowFromField(inputclass);
  } else if (!entry) {
    removeYellowFromField(inputclass);
  } else {
    makeFieldYellow(inputclass);
  }
}


/**
 * Initiated by the event handler, this function initiates the validateEntry
 * function with the appropriate field, 'fullname.'
 */
function runName() {
  validateEntry('fullname');
}

/**
 * Initiated by the event handler, this function initiates the validateEntry
 * function with the appropriate field, 'birthday.'
 */
function runBirthday() {
  validateEntry('birthday');
}

/**
 * Initiated by the event handler, this function initiates the validateEntry
 * function with the appropriate field, 'phone-number.'
 */
function runPhoneNumber() {
  validateEntry('phone-number');
}

/**
 * The event handler activates the event handler by piping the function
 * initiation through the apporiopriate run function. The initiation takes
 * place *after* each keystroke in the appropriate field.
 */
function registerEventHandlers() {
  $('input.fullname').on('keyup', runName);
  $('input.birthday').on('keyup', runBirthday);
  $('input.phone-number').on('keyup', runPhoneNumber);
}

$(document).ready(registerEventHandlers);
