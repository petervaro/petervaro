from dominate.tags import (
    tr,
    td,
    span,
    div,
)
from dominate.util import raw


__all__ = (
    'Job',
)


class Job:

    def __init__(self, toml):
        self._toml = toml

    def _height_in_rows(self):
        assert 'period' in self._toml
        rows = 1
        if 'technologies' in self._toml:
            rows += 1
        if 'company' in self._toml:
            rows += 1
        if 'highlights' in self._toml:
            highlights = self._toml['highlights']
            assert isinstance(highlights, list)
            rows += len(highlights)
        return rows

    @tr
    def _period_and_title(self):
        period = self._toml['period']
        assert isinstance(period, str)
        td(raw(period),
           colspan=1,
           rowspan=self._height_in_rows(),
           class_name='label')

        title = self._toml['title']
        assert isinstance(title, str)
        td(title, colspan=3, class_name='value emphasised')

    @tr
    def _company(self):
        company = self._toml['company']
        assert isinstance(company, str)
        td(raw(company), colspan=3, class_name='value')

    @tr
    def _technologies(self):
        technologies = self._toml['technologies']
        assert isinstance(technologies, list)
        assert len(technologies) >= 1
        technologies = iter(technologies)
        first = next(technologies)
        with td(colspan=3, class_name='value'):
            with div(class_name='details'):
                span(first)
                for technology in technologies:
                    span('+', class_name='delimeter')
                    span(technology)

    def _highlights(self):
        highlights = self._toml['highlights']
        assert isinstance(highlights, list)
        for highlight in highlights:
            with tr() as row:
                with td(colspan=3, class_name='value'):
                    div(highlight, class_name='details highlight')
            yield row

    def as_rows(self):
        assert isinstance(self._toml, dict)
        yield self._period_and_title()
        if 'company' in self._toml:
            yield self._company()
        if 'technologies' in self._toml:
            yield self._technologies()
        if 'highlights' in self._toml:
            yield from self._highlights()
