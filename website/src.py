from pathlib import Path
from datetime import datetime

from tomlkit import loads
from dominate.tags import (
    html,
    head,
    title,
    meta,
    link,
    style,
    script,
    body,
    a,
    p,
    div,
    comment,
    span,
)
from dominate.util import raw

from shared import SHARED


__all__ = (
    'site',
)


#------------------------------------------------------------------------------#
def _block(profession, toml):
    with div(id=profession):
        with div(class_name='content'):
            with div(id=f'{profession}-logo'):
                for style, token in toml['logo']['tokens']:
                    span(raw(token), class_name=style)
            with div(class_name='text'):
                with div(class_name='biography'):
                    for paragraph in toml['biography']['paragraphs']:
                        p(paragraph)
                with div(class_name='links'):
                    for link in toml['links']:
                        a(link['label'], href=link['url'], target='_blank')
                        p(link['summary'])

#------------------------------------------------------------------------------#
def site():
    base = Path('website')
    with (base/'content'/'index.toml').open() as toml, \
         (base/'style'/'index.css').open() as css:
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
                link(rel='shortcut icon', type='image/x-icon', href='favicon.ico')
                link(rel='icon', type='image/x-icon', href='favicon.ico')
                style(raw(css.read()))
                script(src='website/js/anim.js')
                script(src='website/js/index.js')

            with body():
                _block('engineer', data['engineer'])
                _block('designer', data['designer'])
                with div(id='handler'):
                    div(raw('&laquo;&raquo;'))
                script('main();', type='text/javascript')

    copyright = comment(f'Copyright (C) 2015 - {datetime.now().year} '
                        f'{SHARED.info.person_name}. '
                        'All rights reserved.')
    return f'<!DOCTYPE html>{copyright}{document.render(pretty=False)}'
