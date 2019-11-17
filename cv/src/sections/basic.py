from dominate.tags import (
    tr,
    td,
    a,
)

from shared import SHARED


__all__ = (
    'Basic',
)


class Basic:

    def __init__(self, toml):
        self._toml = toml

    @tr
    def _title(self):
        title = self._toml['title']
        assert isinstance(title, str)
        td(title, colspan=4, class_name='title')

    @tr
    def _person(self):
        person = self._toml['person']
        assert isinstance(person, dict)

        label = person['label']
        assert isinstance(label, str)
        td(label, colspan=1, class_name='label')

        td(SHARED.info.person_name, colspan=3, class_name='value')

    def _contact(self):
        contact = self._toml['contact']
        assert isinstance(contact, dict)

        with tr() as row:
            label = contact['label']
            assert isinstance(label, str)
            td(label, rowspan=2, colspan=1, class_name='label')

            contact_points = contact['value']
            assert isinstance(contact_points, dict)

            email = contact_points['email']
            assert isinstance(email, str)
            with td(colspan=3, class_name='value'):
                a(email, href=f'mailto:{email}', target='_blank')

        yield row

        with tr() as row:
            url = contact_points['url']
            assert isinstance(url, str)
            with td(colspan=3, class_name='value'):
                a(url, href=url, target='_blank')

        yield row

    def as_rows(self):
        assert isinstance(self._toml, dict)

        yield self._title()
        yield self._person()
        yield from self._contact()
