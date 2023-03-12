
class InvalidIndexOnBoardError(Exception):
    "Raised when the index specified does not belong within the board"
    pass


class TileFactoryDoesNotExist(Exception):
    "Raised when the given type of the tile factory does not exist"
    pass