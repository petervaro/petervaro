#include <stddef.h>                 /* NULL */
#include <stdlib.h>                 /* EXIT_FAILURE, EXIT_SUCCESS */
#include "human/life.h"             /* state, BREATHING */
#include "human/person/behaviour.h" /* seek, Meaning */

int
main(void)
{
    Meaning *meaning = NULL;

    while (state() == BREATHING)
        meaning = seek();

    if (meaning)
        return EXIT_SUCCESS;
    return EXIT_FAILURE;
}
