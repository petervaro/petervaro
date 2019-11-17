from itertools import zip_longest

from dominate.tags import (
    tr,
    td,
)

from .value import Value


__all__ = (
    'GroupsSideBySide',
)


class GroupsSideBySide:

    def __init__(self, left_toml=None, right_toml=None):
        self._left_toml = left_toml
        self._right_toml = right_toml

    def _columns_of_first_row(self, row_span, label, value):
        assert isinstance(label, str)
        yield td(label, colspan=1, rowspan=row_span, class_name='label')
        yield Value(value).as_column()

    def _rows_of_side(self, side):
        assert isinstance(side, dict) and side

        values = side['value']
        assert isinstance(values, list) and values

        row_span = len(values)
        values = iter(values)

        label = side['label']
        assert isinstance(label, str)

        row = tr()
        for column in self._columns_of_first_row(row_span, label, next(values)):
            row.add(column)

        yield row

        for value in values:
            row = tr()
            row.add(Value(value).as_column())
            yield row

    def _only_left(self):
        return self._rows_of_side(self._left_toml)

    def _only_right(self):
        return self._rows_of_side(self._right_toml)

    def _both_left_and_right(self):
        assert isinstance(self._left_toml, dict) and self._left_toml
        assert isinstance(self._right_toml, dict) and self._right_toml

        left_label = self._left_toml['label']
        assert isinstance(left_label, str)

        left_values = self._left_toml['value']
        assert isinstance(left_values, list) and left_values

        right_label = self._right_toml['label']
        assert isinstance(right_label, str)

        right_values = self._right_toml['value']
        assert isinstance(right_values, list) and right_values

        row_span = max(len(left_values), len(right_values))

        left_values = iter(left_values)
        right_values = iter(right_values)

        row = tr()
        label = self._left_toml['label']
        for column in self._columns_of_first_row(row_span, label, next(left_values)):
            row.add(column)

        label = self._right_toml['label']
        for column in self._columns_of_first_row(row_span, label, next(right_values)):
            row.add(column)

        yield row

        for left_value, right_value in zip_longest(left_values, right_values):
            row = tr()
            if left_value is None:
                row.add(td(class_name='value'))
            else:
                row.add(Value(left_value).as_column())

            if right_value is not None:
                row.add(Value(right_value).as_column())

            yield row

    def as_rows(self):
        if self._left_toml is None and \
           self._right_toml is None:
                return
        elif self._left_toml is None:
            return self._only_right()
        elif self._right_toml is None:
            return self._only_left()
        else:
            return self._both_left_and_right()
