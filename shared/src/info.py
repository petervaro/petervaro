__all__ = ('Info',)


#------------------------------------------------------------------------------#
class Info:

    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    def __init__(self, toml):
        self.person_name = toml['name']