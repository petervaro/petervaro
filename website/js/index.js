/* PRE **
** PRE */

/*----------------------------------------------------------------------------*/
function main()
{
    'use strict';

    /* Temporary variables */
    var engineer = document.getElementById('engineer'),
        designer = document.getElementById('designer');

    /* Constants */
    var HTML = document.documentElement,
        REM = parseFloat(window.getComputedStyle(HTML).fontSize),
        MOUSE_X,
        REQUEST_ID,
        LEFT_ARROW = 37,
        UP_ARROW = 38,
        RIGHT_ARROW = 39,
        DOWN_ARROW = 40,
        MOVE_RANGE = 128,
        SCROLL_DELTA = 32,
        CONTENT_WIDTH = 30*REM,
        CONTENT_HEIGHT = 48*REM,
        BODY = document.body,
        HANDLER = document.getElementById('handler'),
        HANDLER_STYLE = HANDLER.style,
        ENGINEER_STYLE = engineer.style,
        DESIGNER_STYLE = designer.style,
        ENGINEER_CONTENT_STYLE = engineer.getElementsByClassName('content')[0].style,
        DESIGNER_CONTENT_STYLE = designer.getElementsByClassName('content')[0].style;


    /*- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - */
    /* Helper functions */
    function px(value)
    {
        return value.toString() + 'px';
    }


    /*- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - */
    function getPageWidth()
    {
        return Math.max(BODY.scrollWidth,
                        BODY.offsetWidth,
                        HTML.clientWidth,
                        HTML.scrollWidth,
                        HTML.offsetWidth);
    }


    /*- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - */
    function getPageHeight()
    {
        return Math.max(BODY.scrollHeight,
                        BODY.offsetHeight,
                        HTML.clientHeight,
                        HTML.scrollHeight,
                        HTML.offsetHeight);
    }


    /*- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - */
    function resize(mouseX)
    {
        /* Limit mouse movement */
        if (mouseX <  0 ||
            mouseX >= (window.innerWidth ||
                       document.documentElement.clientWidth ||
                       document.body.clientWidth))
                return;

        /* Update global state */
        MOUSE_X = mouseX;

        /* Calculate essential values */
        var pageWidth = getPageWidth(),
            contentLeft = (pageWidth - CONTENT_WIDTH)/2.0,
            opacity = (mouseX - Math.floor(contentLeft))/CONTENT_WIDTH;

        /* Set style attributes */
        HANDLER_STYLE.left =
        DESIGNER_STYLE.left =
        ENGINEER_STYLE.width = px(mouseX);
        DESIGNER_STYLE.width = px(pageWidth - mouseX);

        ENGINEER_CONTENT_STYLE.left = px(contentLeft);
        DESIGNER_CONTENT_STYLE.left = px(contentLeft - mouseX);

        ENGINEER_CONTENT_STYLE.top =
        DESIGNER_CONTENT_STYLE.top = px((getPageHeight() - CONTENT_HEIGHT)/2.0);

        if (opacity <= 0.0)
            opacity = 0.0;
        else if (opacity >= 1.0)
            opacity = 1.0;

        ENGINEER_CONTENT_STYLE.opacity = opacity.toString();
        DESIGNER_CONTENT_STYLE.opacity = (1.0 - opacity).toString();
    }


    /*- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - */
    /* Handler animation functions */
    var MIN = 0.0,
        MAX = 1.0,
        STEP = 0.035,
        VALUE = MIN;
    function pulse()
    {
        var next = VALUE + STEP;
        if (next > MAX ||
            next < MIN)
                STEP *= -1.0;
        return VALUE += STEP;
    }


    /*- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - */
    function reset()
    {
        var next = VALUE + STEP;
        if (next > VALUE)
            STEP *= -1.0;
        if (next <= MIN)
            return MIN;
        return VALUE += STEP;
    }


    /*- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - */
    function update(value)
    {
        /* Calculate next animation phase */
        var size = Math.floor((value + 1)*40.0);

        /* Set values */
        HANDLER_STYLE.width =
        HANDLER_STYLE.height = px(size);
        HANDLER_STYLE.marginTop =
        HANDLER_STYLE.marginLeft = px(-(size/2.0));
        HANDLER_STYLE.opacity = (0.5 + (1.0 - value)*0.5).toString();
    }


    /*- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - */
    function loopPulse()
    {
        REQUEST_ID = window.requestAnimationFrame(loopPulse);
        update(pulse());
    }


    /*- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - */
    function resetPulse()
    {
        var value = reset();
        if (value === MIN)
            window.cancelAnimationFrame(REQUEST_ID);
        else
        {
            REQUEST_ID = window.requestAnimationFrame(resetPulse);
            update(value);
        }
    }


    /*- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - */
    /* Set callbacks */
    window.addEventListener('resize', function ()
    {
        resize(MOUSE_X || 0.0);
    });


    /*- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - */
    function onMouseMove(event)
    {
        event.preventDefault();
        HANDLER_STYLE.top = px(event.pageY);
        resize(event.pageX);
    }

    /* Handle mouse events */
    HANDLER.addEventListener('mouseenter', function (event)
    {
        window.cancelAnimationFrame(REQUEST_ID);
        loopPulse();
    });
    HANDLER.addEventListener('mouseleave', function (event)
    {
        window.cancelAnimationFrame(REQUEST_ID);
        resetPulse();
    });
    HANDLER.addEventListener('mousedown', function (event)
    {
        HTML.style.cursor = 'col-resize';
        document.addEventListener('mousemove', onMouseMove);
    });
    document.addEventListener('mouseup', function ()
    {
        HTML.style.cursor = 'default';
        document.removeEventListener('mousemove', onMouseMove);
    });


    /*- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - */
    HTML.addEventListener('wheel', function (event)
    {
        /* Normalize scroll-wheel move */
        if (event.deltaY < 0)
            /* Slide page-separator */
            return resize(MOUSE_X - SCROLL_DELTA);
        return resize(MOUSE_X + SCROLL_DELTA);
    });


    /*- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - */
    HTML.addEventListener('keydown', function (event)
    {
        switch (event.keyCode)
        {
            case UP_ARROW:
            case LEFT_ARROW:
                return resize(MOUSE_X - SCROLL_DELTA);
            case DOWN_ARROW:
            case RIGHT_ARROW:
                return resize(MOUSE_X + SCROLL_DELTA);
        }
    });


    /*- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - */
    function onTouchMove(event)
    {
        if (event.changedTouches.length >= 2)
            return;
        event.preventDefault();
        resize(event.changedTouches[0].pageX);
    }

    /* Handle touch events */
    document.addEventListener('touchstart', function ()
    {
        window.cancelAnimationFrame(REQUEST_ID);
        resetPulse();
        document.addEventListener('touchmove', onTouchMove);
    });

    document.addEventListener('touchend', function ()
    {
        document.removeEventListener('touchmove', onTouchMove);
    });


    /*- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - */
    /* Initial calls */
    resize(getPageWidth()/2);
    loopPulse();
}
