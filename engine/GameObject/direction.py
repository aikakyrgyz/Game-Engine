
class Direction:
    def __init__(self, dx, dy, direction):
        self.dx = dx
        self.dy = dy
        self.direction = direction

    def get_dx(self):
        return self.dx

    def get_dy(self):
        return self.dy

    def __str__(self):
        return self.direction

# UP = Direction(0, 1, "UP")
DOWN = Direction(0, -1, "DOWN")
LEFT = Direction(-1, 0, "LEFT")
RIGHT = Direction(1, 0, "RIGHT")
ROTATE = Direction(0,0, "ROTATE")


