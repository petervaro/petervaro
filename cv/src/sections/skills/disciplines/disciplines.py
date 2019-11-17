from itertools import zip_longest

from .groups import GroupsSideBySide


__all__ = (
    'DisciplinesSideBySide',
)


class DisciplinesSideBySide:

    _GROUPS = 'specialist', 'enthusiast', 'explorer', 'tools', 'other'

    def __init__(self, left_toml=None, right_toml=None):
        self._left_toml = left_toml
        self._right_toml = right_toml

    def _only_left(self):
        assert isinstance(self._left_toml, dict)
        for group in self._GROUPS:
            try:
                group_toml = self._left_toml[group]
            except KeyError:
                continue
            else:
                yield from GroupsSideBySide(group_toml, None).as_rows()

    def _only_right(self):
        assert isinstance(self._right_toml, dict)
        for group in self._GROUPS:
            try:
                group_toml = self._right_toml[group]
            except KeyError:
                continue
            else:
                yield from GroupsSideBySide(None, group_toml).as_rows()

    def _both_left_and_right(self):
        assert isinstance(self._left_toml, dict)
        assert isinstance(self._right_toml, dict)

        for group in self._GROUPS:
            yield from GroupsSideBySide(self._left_toml.get(group),
                                        self._right_toml.get(group)).as_rows()

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
