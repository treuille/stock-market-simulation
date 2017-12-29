// Autoloads the content of inner-index.html into index.html every 300ms.

// Some magic to let us use ES6 here.
(function(){
  'use strict';

  // Run this when the page loads.
  function main() {
  };

  // Run this when the page loads.
  $(document).ready(() => {
    const POLL_MILLISECONDS = 100.0
    let previous_result = ""
    console.log('Starting load loop.')

    setInterval(() => {
      console.log('Polling');

      $.ajax('dynamic.html')
      .done((result) => {
        if (result != previous_result) {
          console.log('The previous result changed.')
          $('.dynamic-html-container').html(result);
        } else {
          console.log("The previous result didn't change.");
        }
        previous_result = result
      })
      .fail(( xhr, status, errorThrown ) => {
        console.log( "Sorry, there was a problem! " + errorThrown + " " + status);
      });
    }, POLL_MILLISECONDS);

    const invk = (v) => v * 2;
    console.log(invk(1233));
  });

})();
