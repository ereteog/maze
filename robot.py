from elems import Elem, Wall, Door, Exit, Free

class Robot(Elem):

    def __init__(self, pos, symb='X'):
        Elem.__init__(self, symb)
        self.pos = pos

    def moveN(self, direction, n):
        for i in range(n):
            self.move(direction)

    def move(self, direction):
        row = self.pos.row
        col = self.pos.col
        if direction == 'N':
            row -= 1
        elif direction == 'S':
            row += 1
        elif direction == 'W':
            col -= 1
        elif direction == 'E':
            col += 1

        try:
            next_elem = self.pos.maze.elem(row, col)
            if type(next_elem) in {Door, Exit, Free}:
                self.pos.row = row
                self.pos.col = col
                self.pos.elem = next_elem
            elif type(next_elem) is Wall:
                raise MoveError("I can't cross wall, I'm just a weak robot :-(")
            else:
                raise MoveError("I'm scared, I've never seen this kind of element")
        except IndexError:
            print("hey, you can't get out of the maze here!")

class Position:

    def __init__(self, maze, row, col, elem):
        self.maze = maze
        self.row = row
        self.col = col
        self.elem = elem

class MoveError(Exception):
    pass
