/* INFO **
** INFO */

/*----------------------------------------------------------------------------*/
/* Set requestAnimationFrame method, based on:
   - http://paulirish.com/2011/requestanimationframe-for-smart-animating/
   - http://my.opera.com/emoller/blog/2011/12/20/requestanimationframe-for-smart-er-animating */
(function ()
{
    "use strict";

    var lastTime = 0,
        prefix,
        prefices = ['ms', 'moz', 'webkit', 'o'];

    /* Try to set method */
    for (var i=0; i<prefices.length; ++i)
    {
        prefix = prefices[i];
        window.requestAnimationFrame = window[prefix + 'RequestAnimationFrame'];
        if ((window.cancelAnimationFrame  =
                 window[prefix + 'CancelAnimationFrame'] ||
                 window[prefix + 'CancelRequestAnimationFrame']))
            return;
    }

    /* If methods are not available */
    window.requestAnimationFrame = function(callback, element)
    {
        var currTime   = new Date().getTime(),
            timeToCall = Math.max(0, 16 - (currTime - lastTime)),
            id = window.setTimeout(function()
            {
                callback(currTime + timeToCall);
            }, timeToCall);

        lastTime = currTime + timeToCall;
        return id;
    };

    window.cancelAnimationFrame = function(id)
    {
        window.clearTimeout(id);
    };
})();
