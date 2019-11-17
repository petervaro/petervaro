from pathlib import Path
from subprocess import run

from htmlmin import minify

from .src import site


__all__ = (
    'build',
)


#------------------------------------------------------------------------------#
def build():
    base = Path('website')
    run(('npx', 'sass', str(base/'style'/'index.scss'),
                        str(base/'style'/'index.css'),
                        '--no-source-map',
                        '--style', 'compressed'),
        check=True,
        capture_output=True)

    with Path('index.html').open('w') as target:
        target.write(minify(site()))
