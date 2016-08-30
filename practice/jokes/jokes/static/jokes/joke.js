'use strict';

/**
 * Reveals all the punchlines.
 *
 * I must figure out a way to only reveal any given punchline...
 */
function revealPunchline() {
  $('.punchline').show();
  atomicText.hide();
}

/**
 * Hides all the punchlines.
 *
 * I must figure out a way to only hide any given punchline...
 */
function hidePunchline() {
  $('.punchline').hide();
  atomicText.hide();
}


/**
 * Registers the event handlers so punchlines are revealed on the click of any setup. And punchlines are all hidden if
 * clicked on.
 *
 * I must figure out a way to only reveal any given punchline for any given setup...
 */
function registerEventHandlers() {
  $('.setup').on('click', revealPunchline);
  $('.punchline').on('click', hidePunchline);
   }

$(document).ready(function() {
  registerEventHandlers();
  hidePunchline();
});