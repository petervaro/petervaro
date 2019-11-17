from pathlib import Path
from itertools import chain
from datetime import datetime

from tomlkit import loads

from dominate.tags import (
    html,
    head,
    meta,
    title,
    body,
    table,
    style,
    tr,
    td,
    img,
    div,
    comment,
)
from dominate.util import raw

from shared import SHARED

from .sections import (
    Basic,
    Skills,
    Experience,
    Education,
)


__all__ = (
    'cv',
)


def cv():
    base = Path('cv')
    with (base / 'content' / 'data.toml').open() as toml, \
         (base / 'style' / 'index.css').open() as css:
        data = loads(toml.read())
        with html(lang='en') as document:
            with head():
                meta(charset='utf-8')
                meta(name='description',
                     content=f'{SHARED.info.person_name} (engineer|designer)')
                meta(name='keywords',
                     content=','.join(SHARED.meta.keywords))
                meta(name='author',
                     content=f'{SHARED.info.person_name}')
                title(SHARED.info.person_name)
                style(raw(css.read()))
            with body():
                with table(id='content') as content:
                    with tr():
                        with td(id='image', colspan=4):
                            img(src='img/header.png', alt='...')
                            div('Curriculum Vitae')
                for row in chain(Basic(data['basic']).as_rows(),
                                 Skills(data['skills']).as_rows(),
                                 Experience(data['experience']).as_rows(),
                                 Education(data['education']).as_rows()):
                    content.add(row)

    copyright = comment(f'Copyright (C) 2015 - {datetime.now().year} '
                        f'{SHARED.info.person_name}. '
                        'All rights reserved.')
    return f'<!DOCTYPE html>{copyright}{document.render(pretty=False)}'
