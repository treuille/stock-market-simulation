// Autoloads the content of inner-index.html into index.html every 300ms.

// Some magic to let us use ES6 here.
(function(){
  'use strict';

  // Run this when the page loads.
  $(document).ready(() => {
    const POLL_MILLISECONDS = 100.0

    // Loop continuously, polling for changes to dynamic.html.
    let previous_result = ""
    setInterval(() => {
      $.ajax('dynamic.html')
      .done((result) => {
        if (result != previous_result) {
          $('.dynamic-html-container').html(result);
        }
        previous_result = result
      })
      .fail((xhr, status, errorThrown) => {
        // Put in error handling code here.
      });
    }, POLL_MILLISECONDS);
  });

})();
