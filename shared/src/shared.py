from pathlib import Path

from tomlkit import loads

from .meta import Meta
from .info import Info


__all__ = ('Shared',)


#------------------------------------------------------------------------------#
class Shared:

    _DATA = Path('shared') / 'content' / 'data.toml'
    FAVICON_PNG = Path('shared') / 'img' / 'favicon.png'

    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    def __init__(self):
        with self._DATA.open() as file:
            toml = loads(file.read())
            self.meta = Meta(toml['meta'])
            self.info = Info(toml['info'])
