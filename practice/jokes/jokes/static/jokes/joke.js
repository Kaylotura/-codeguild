'use strict';


/**
 * Reveals any hidden sibling elements as the item clicked. This should only reveal the punchline within any given
 * joke div, as that punchlines are the only hidden element, and setups are the only other element, and they're what is
 * to be clicked on.
 */
function revealPunchline() {
  $(this).siblings().show();
}

/**
 * Hides the element that has been clicked. This should only be used on any given punchline.
 */
function hidePunchline() {
  $(this).hide();
}


/**
 * Registers the event handlers, allowing any setup element to be clicked on to reveal the punchline, and any punchline
 * element may be clicked on in order to hide said punchline.
 */
function registerEventHandlers() {
  $('.setup').on('click', revealPunchline);
  $('.punchline').on('click', hidePunchline);
  }

$(document).ready(function() {
  $('.punchline').hide();
  registerEventHandlers();
});
