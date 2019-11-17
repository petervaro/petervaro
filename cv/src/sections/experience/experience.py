from dominate.tags import (
    tr,
    td,
)

from .job import Job


__all__ = (
    'Experience',
)


class Experience:

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

        jobs = self._toml['jobs']
        assert isinstance(jobs, list)
        for job in jobs:
            yield from Job(job).as_rows()
