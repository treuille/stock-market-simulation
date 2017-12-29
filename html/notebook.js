// Autoloads the content of inner-index.html into index.html every 300ms.

// Some magic to let us use ES6 here.
(function(globals) {
  'use strict';

  // Dictionary of exported functions
  globals.notebook = {

    // Excectuion starts here when the document is ready.
    main: () => {
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
    },

    // Call this funtion style the rows and headers of a data table properly.
    style_data_frame: (id) => {
      console.log('styling', id);
      $('#' + id).DataTable({
        fixedHeader: true,
        lengthChange: false,
        pageLength: 5,
      });
    },
  };

  // Run main when the page loads.
  $(document).ready(notebook.main);

})(this);
