'use strict';

/**
 * The Validator takes in the users input as they type into the form in
 * index.html and uses events to visually que the user that their input is not
 * valid, by filling the field with a yellow background. Once the the entry is
 * valid the background returns to white.
 */

var NAME_STUCTURE = /((\w+)\s(\w+))/;
var BIRTHDAY_STRUCTURE = /(\d\d)\-(\d\d)\-(\d\d\d\d)/;
var PHONE_NUMBER_STRUCTURE = /(\d\d\d)\-(\d\d\d)\-(\d\d\d\d)/;
var nameEntry = document.getElementsByClassName('name').value;
var phoneNumberEntry = document.getElementsByClassName('phone-number').value;
var birthdayEntry = document.getElementsByClassName('birthday').value;

/**
 *
 */
function validateName() {
  return NAME_STUCTURE.test(nameEntry);
}

/**
 *
 */
function validatePhoneNumber() {
  return PHONE_NUMBER_STRUCTURE.test(phoneNumberEntry);
}

/**
 *
 */
function validateBirthday() {
  return BIRTHDAY_STRUCTURE.test(birthdayEntry);
}

/**
 *
 */
function makeFiekdYellow(field) {
  $('input.' + field).addClass('invalid');
}

/**
 *
 */
function removeYellowFromField(field) {
  $('input.' + field).removeClass('invalid');
}



/**
 *
 */
function checknameValidityWhileTyping() {
  $('name').on('change', function() {
    var nameEntry = document.getElementsByClassName('name').value;
    if (validateName()) {
      removeYellowFromField('name');
    } else {
      makeFiekdYellow('name');
    }
  });
}


$(document).ready(registerEventHandlers);
