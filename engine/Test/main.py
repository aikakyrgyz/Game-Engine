
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
# from engine.Board.tiles_board import TilesBoard
# from engine.Tile.tile import Tile
# from engine.Tile.tileAbstractFactory import TileAbstractFactory
# from engine.Tile.tileFactory import TileFactory
# from Tile.tile import Tile
# from Tile.tileAbstractFactory import TileAbstractFactory
# from Tile.tileFactory import TileFactory
# from engine.Board.tiles_board import TilesBoard


from engine.Tile.empty_tile_factory import EmptyTileFactory
from engine.Tile import Tile
from engine.Board.tiles_board import TilesBoard
from tileAbstractFactory import TileAbstractFactory
from tileFactory import TileFactory


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


# from Sprite import sprite
# from Tile import tileFactory
# In client code

# create concrete factories

# Sprite yellow-sprite = Sprite("yellow-image.png", size)
# Sprite red-sprite = Sprite("red-sprite.png", size)
# yellow = sprite.Sprite("yellow")
# red = sprite.Sprite("red")
# my_yellow_virus_factory = tileFactory.TileFactory(yellow)
# my_red_virus_factory = tileFactory.TileFactory(red)
# factory.register_factory('YELLOW_VIRUS', my_yellow_virus_factory)
# factory.register_factory('RED_VIRUS', my_red_virus_factory)
#
# # now actually create the tile generating it
# yellow_virus_tile = factory.create_tile("YELLOW_VIRUS") # passing the name of the tile factory
# red_virus_tile = factory.create_tile("RED_VIRUS")
#
# print(yellow_virus_tile.__class__)
# print(yellow_virus_tile.get_type())

class YellowVirus(Tile):
    pass

class RedVirus(Tile):
    pass

factory = TileAbstractFactory()
yellow_factory = TileFactory(YellowVirus, "yellow.png")
red_factory = TileFactory(RedVirus, "red.png")

factory.register_factory("YELLOW", yellow_factory)
factory.register_factory("RED", red_factory)

yellow_tile = factory.create_tile("YELLOW")
red_tile = factory.create_tile("RED")


empty = EmptyTileFactory()
empty2 = EmptyTileFactory()
print(type(empty))
print(type(empty2))
print(type(yellow_tile))
print(type(red_tile))

# print(isinstance(red_virus_tile, my_red_virus_factory))



tile_types = [["EMPTY", "EMPTY", "EMPTY"], ["EMPTY", "RED", "EMPTY"], ["YELLOW", "YELLOW", "YELLOW"]]
b = TilesBoard(10, factory, )
b.print_board()

