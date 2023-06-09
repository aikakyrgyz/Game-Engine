from abc import ABC, abstractmethod

from engine.GameObject.direction import Direction


class GameObject(ABC):
    def __init__(self, x, y, width, height, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        # can be any object, ex: mario throwing the capsules who is outside the board
        # speed will have to be a whole integer, since we want to move by tile
        self.speed = speed
        self.direction = Direction.DOWN


    @abstractmethod
    def update(self):
        pass

    # @abstractmethod
    # def draw(self): ...

    # can have different speeds for different directions
    # implement later if needed
    # def set_speed(self, speed):
    #     self.speed = speed
    #
    # def get_speed(self):
    #     return self.speed

    def get_direction(self):
        return self.direction

    # control the speed in the loop
    # def move(self):
    #     if self.speed > 0:
    #         self.x += self.direction.get_dx() * self.speed
    #         self.y += self.direction.get_dy() * self.speed









