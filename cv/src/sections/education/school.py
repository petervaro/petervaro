from dominate.tags import (
    tr,
    td,
    span,
)
from dominate.util import raw


__all__ = (
    'School',
)


class School:

    def __init__(self, toml):
        self._toml = toml

    def _height_in_rows(self):
        assert 'period' in self._toml
        rows = 1
        if 'institution' in self._toml:
            rows += 1
        return rows

    @tr
    def _period_and_faculty(self):
        period = self._toml['period']
        assert isinstance(period, str)
        td(raw(period),
           colspan=1,
           rowspan=self._height_in_rows(),
           class_name='label')

        faculty = self._toml['faculty']
        assert isinstance(faculty, str)
        td(faculty, colspan=3, class_name='value emphasised')

    @tr
    def _institution(self):
        institution = self._toml['institution']
        assert isinstance(institution, str)
        td(institution, colspan=3, class_name='value')

    def as_rows(self):
        assert isinstance(self._toml, dict)
        yield self._period_and_faculty()
        if 'institution' in self._toml:
            yield self._institution()
