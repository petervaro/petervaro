from dominate.tags import (
    tr,
    td,
)

from .school import School


__all__ = (
    'Education',
)


class Education:

    def __init__(self, toml):
        self._toml = toml

    @tr
    def _title(self):
        title = self._toml['title']
        assert isinstance(title, str)
        td(title, colspan=4, class_name='title')

    def as_rows(self):
        assert isinstance(self._toml, dict)
        yield self._title()

        schools = self._toml['schools']
        assert isinstance(schools, list)
        for school in schools:
            yield from School(school).as_rows()
