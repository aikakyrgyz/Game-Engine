# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from Tile.empty_tile_factory import EmptyTileFactory
from Tile.tile import Tile
from Tile.tileAbstractFactory import TileAbstractFactory
from Tile.tileFactory import TileFactory


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


from Sprite import sprite
from Tile import tileFactory
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

factory.register_factory("yellow", yellow_factory)
factory.register_factory("red", red_factory)

yellow_tile = factory.create_tile("yellow")
red_tile = factory.create_tile("red")


empty = EmptyTileFactory()
empty2 = EmptyTileFactory()
print(type(empty))
print(type(empty2))
print(type(yellow_tile))
print(type(red_tile))

# print(isinstance(red_virus_tile, my_red_virus_factory))



