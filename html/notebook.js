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
      let previousResult = "";
      let scrolledToBottom = false;
      setInterval(() => {
        $.ajax('dynamic.html')
        .done((result) => {
          if (result != previousResult) {
            $('.dynamic-html-container').html(result);
            scrolledToBottom = false;
          } else if (!scrolledToBottom) {
            notebook.scrollToBottom()
            scrolledToBottom = true;
          }
          previousResult = result
        })
        .fail((xhr, status, errorThrown) => {
          if (!scrolledToBottom)
            notebook.scrollToBottom()
          scrolledToBottom = true;
        });
      }, POLL_MILLISECONDS);
    },

    // Call this funtion style the rows and headers of a data table properly.
    styleDataFrame: (id) => {
      // Turn on scrollX only when there are > 6 columns.
      const numColumns = $(`#${id} tr`).first().children().length
      const scrollX = numColumns > 7

      // Style the table.
      $(`#${id}`)
      .addClass('display')
      .css({fontFamily: 'monospace'})
      .DataTable({
        paging: false,
        scrollY: true, // 400,
        scrollX: scrollX,
        searching: false,
      });

      // Style each cell.
      $(`#${id} td`)
      .css({textAlign: 'right'})
    },

    // Animate a scroll right down to the bottom.
    scrollToBottom: () => {
      setTimeout(() => {
        $("html, body").animate({
          scrollTop: $(document).height() }, 500);
        console.log('Scrolled to bottom.');
      }, 50);
    },
  };



  // Run main when the page loads.
  $(document).ready(notebook.main);

})(this);
