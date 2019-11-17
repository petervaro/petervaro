from dominate.tags import (
    td,
    span,
)
from dominate.util import text


class Value:

    def __init__(self, value):
        self._value = value

    def _simple_text(self):
        assert isinstance(self._value, str)
        if not self._value:
            return
        return td(self._value, colspan=1, class_name='value')

    def _delimited_text(self):
        assert isinstance(self._value, list)
        if not self._value:
            return

        values = iter(self._value)
        with td(colspan=1, class_name='value') as column:
            text(next(values))
            for value in values:
                span('/', class_name='delimeter')
                text(value)

        return column

    def as_column(self):
        if isinstance(self._value, str):
            return self._simple_text()
        elif isinstance(self._value, list):
            return self._delimited_text()
        else:
            assert False, self._value.__class__.__name__
