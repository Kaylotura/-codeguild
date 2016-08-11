'use strict';

/**
 * The Validator takes in the users input as they type into the form in
 * index.html and uses events to visually que the user that their input is not
 * valid, by filling the field with a yellow background. Once the the entry is
 * valid the background returns to white.
 */

var NAME_STUCTURE = /(\w+)\s(\w+)/;
var BIRTHDAY_STRUCTURE = /(\d\d)\-(\d\d)\-(\d\d\d\d)/;
var PHONE_NUMBER_STRUCTURE = /(\d\d\d)\-(\d\d\d)\-(\d\d\d\d)/;

/**
 *
 */
function validateName(entry) {
  return NAME_STUCTURE.test(entry);
}

/**
 *
 */
function validatePhoneNumber(entry) {
  return PHONE_NUMBER_STRUCTURE.test(entry);
}

/**
 *
 */
function validateBirthday(entry) {
  return BIRTHDAY_STRUCTURE.test(entry);
}

/**
 *
 */
function toggleFieldYellow(field) {
  $('input.' + field).toggleClass('invalid');
}
