// Autoloads the content of inner-index.html into index.html every 300ms.

// Some magic to let us use ES6 here.
(function(){
  'use strict';

  // Run this when the page loads.
  function main() {
  };

  // Run this when the page loads.
  $(document).ready(() => {
    let innerHtml = ""
    console.log('Starting load loop.')

    $.ajax('dynamic.html')
    .done((result) => {
      console.log('Success');
      console.log(result);
    })
    .fail(( xhr, status, errorThrown ) => {
      console.log( "Sorry, there was a problem!" );
      console.log( "Error: " + errorThrown );
      console.log( "Status: " + status );
      console.dir( xhr );
    });

    const invk = (v) => v * 2;
    console.log(invk(1233));
  });

})();
