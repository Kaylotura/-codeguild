'use strict';

/**
 * The Validator takes in the users input as they type into the form in
 * index.html and uses events to visually que the user that their input is not
 * valid, by filling the field with a yellow background. Once the the entry is
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
 * Begins by checking the entry in fullname class text box on the form,
 * then proceeds to run that value through a validation process.
 */
function runName() {
  var nameEntry = $('input.fullname').prop('value');
 /**
  * If the entry in the full name class text box is valid or empty, the
  * invalid class is turned off for that textbox, but otherwise it is turned
  * on.
  */
  function validateName(nameEntry) {
    return /(\w+)\s(\w+)/.test(nameEntry);
  }
  if (validateName(nameEntry)) {
    removeYellowFromField('fullname');
  } else if (!nameEntry) {
    removeYellowFromField('fullname');
  } else {
    makeFieldYellow('fullname');
  }
}

/**
* Begins by checking the entry in phone-number class text box on the form,
* then proceeds to run that value through a validation process.
 */
function runPhoneNumber() {
  var phoneNumberEntry = $('input.phone-number').prop('value');
  /**
   * If the entry in the phone number class text box is valid or empty, the
   * invalid class is turned off for that textbox, but otherwise it is turned
   * on.
   */
  function validatePhoneNumber() {
    return /(\d\d\d)\-(\d\d\d)\-(\d\d\d\d)/.test(phoneNumberEntry);
  }
  if (validatePhoneNumber(phoneNumberEntry)) {
    removeYellowFromField('phone-number');
  } else if (!phoneNumberEntry) {
    removeYellowFromField('phone-number');
  } else {
    makeFieldYellow('phone-number');
  }
}

/**
* Begins by checking the entry in birthday class text box on the form,
* then proceeds to run that value through a validation process.
 */
function runBirthday() {
  var birthdayEntry = $('input.birthday').prop('value');
  console.dir(birthdayEntry);
 /**
  * If the entry in the phone number class text box is valid or empty, the
  * invalid class is turned off for that textbox, but otherwise it is turned
  * on.
  */
  function validateBirthday() {
    return /(\d\d\d\d)\-(\d\d)\-(\d\d)/.test(birthdayEntry);
  }
  if (validateBirthday(birthdayEntry)) {
    removeYellowFromField('birthday');
  } else if (!birthdayEntry) {
    removeYellowFromField('birthday');
  } else {
    makeFieldYellow('birthday');
  }
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
