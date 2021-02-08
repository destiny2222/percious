(function ($) {
    "use strict";
    
        // preloader
        $(window).on('load', function () {
            $('#preloader').delay(350).fadeOut('slow');
            $('body').delay(350).css({ 'overflow': 'visible' });
        })
    
        
       

    })(jQuery);

   