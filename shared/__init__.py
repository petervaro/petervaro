from subprocess import run

from .src import SHARED


__all__ = (
    'SHARED',
    'build',
)


def build():
    run(('convert', str(SHARED.FAVICON_PNG),
                    '-colors', '256',
                    '-background', 'transparent',
                    'favicon.ico'),
        check=True,
        capture_output=True)
