'use strict';

/**
 * The Validator takes in the user's input as they type into the form and
 * uses kestroke events to visually que the user that their input is not
 * valid by filling the field with a yellow background. Once the the entry is
 * valid the background returns to white.
 *
 * Currently there are many patterns that need to be taken care of.
 */

/**
 * Adds the invalid class to the given input field which has a yellow
 * background in its properties.
 */
function makeFieldYellow(field) {
  $('input.' + field).addClass('invalid');
}

/**
 * Removes the yellow-background invalid class from an input field.
 */
function removeYellowFromField(field) {
  $('input.' + field).removeClass('invalid');
}

/**
 * Takes in an entry, and the field it came from and returns whether it is a
 * valid entry or not.
 */
function checkIfValid(field, entry) {
  if (field === 'fullname') {
    return /(\w+)\s(\w+)/.test(entry);
  } else if (field === 'birthday') {
    return /(\d\d\d\d)\-(\d\d)\-(\d\d)/.test(entry);
  } else if (field === 'phone-number') {
    return /(\d\d\d)\-(\d\d\d)\-(\d\d\d\d)/.test(entry);
  }
}


/**
 * Begins by checking the entry in fullname class text box on the form,
 * then proceeds to run that value through a validation process.
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


function runName() {
  validateEntry('fullname');
}

function runBirthday() {
  validateEntry('birthday');
}

function runPhoneNumber() {
  validateEntry('phone-number');
}

/**
 * The even handler run the validation that the user is typing indirectly after
 * each keystroke.
 */
function registerEventHandlers() {
  $('input.fullname').on('keyup', runName);
  $('input.birthday').on('keyup', runBirthday);
  $('input.phone-number').on('keyup', runPhoneNumber);
}

$(document).ready(registerEventHandlers);
