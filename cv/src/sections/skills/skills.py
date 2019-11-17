from dominate.tags import (
    tr,
    td,
)

from .disciplines import DisciplinesSideBySide


__all__ = (
    'Skills',
)


class Skills:

    def __init__(self, toml):
        self._toml = toml

    def as_rows(self):
        engineer = self._toml['engineer']
        designer = self._toml['designer']

        with tr() as row:
            td(engineer['title'], colspan=2, class_name='title')
            td(designer['title'], colspan=2, class_name='title')

        yield row

        yield from DisciplinesSideBySide(engineer, designer).as_rows()
