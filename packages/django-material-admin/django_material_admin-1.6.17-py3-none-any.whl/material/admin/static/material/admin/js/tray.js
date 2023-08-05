(function ($) {

    var navBarIcon = $('.tray-nav-bar.material-icons');
    var additionalSubmitLineIcon = $('.tray-additional-submit-row.material-icons');
    var toolsIcon = $('.tray-object-tools.material-icons');
    var navBarCookie = 'tray-nav-bar';
    var additionalSubmitLineCookie = 'additional-submit-line';
    var toolsCookie = 'object-tools';

    function createCookie(name, value, days) {
        var expires;

        if (days) {
            var date = new Date();
            date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
            expires = "; expires=" + date.toGMTString();
        } else {
            expires = "";
        }
        document.cookie = encodeURIComponent(name) + "=" + encodeURIComponent(value) + expires + "; path=/";
    }

    function readCookie(name) {
        var nameEQ = encodeURIComponent(name) + "=";
        var ca = document.cookie.split(';');
        for (var i = 0; i < ca.length; i++) {
            var c = ca[i];
            while (c.charAt(0) === ' ')
                c = c.substring(1, c.length);
            if (c.indexOf(nameEQ) === 0)
                return decodeURIComponent(c.substring(nameEQ.length, c.length));
        }
        return null;
    }

    function eraseCookie(name) {
        createCookie(name, "", -1);
    }

    navBarIcon.on('click', function () {
        eraseCookie(navBarCookie);
        location.reload();
    });
    $('.nav-bar.minimize').on('click', function () {
        createCookie(navBarCookie, true, 1000);
        location.reload();
    });

    toolsIcon.on('click', function () {
        readCookie(toolsCookie)
            ? eraseCookie(toolsCookie)
            : createCookie(toolsCookie, true, 1000);
        location.reload();
    });
     $('.tools.minimize').on('click', function () {
        readCookie(toolsCookie)
            ? eraseCookie(toolsCookie)
            : createCookie(toolsCookie, true, 1000);
        location.reload();
    });

    additionalSubmitLineIcon.on('click', function () {
        readCookie(additionalSubmitLineCookie)
            ? eraseCookie(additionalSubmitLineCookie)
            : createCookie(additionalSubmitLineCookie, true, 1000);

        location.reload();
    });
    $('.submit-line.minimize').on('click', function () {
        readCookie(additionalSubmitLineCookie)
            ? eraseCookie(additionalSubmitLineCookie)
            : createCookie(additionalSubmitLineCookie, true, 1000);
        location.reload();
    });

})(jQuery);
