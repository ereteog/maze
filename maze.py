from elems import Wall, Door, Exit, Free
from robot import Robot, Position

class Maze:


    default_char = {"O":Wall,
                    ".":Door,
                    "U":Exit,
                    " ":Free,
                    "X":Robot}

    def __init__(self,
                 maze_file=None,
                 robot=None,
                 symbs={},
                 char_classes=default_char):
        self.robot = robot
        self._elems = []
        self._char_classes=char_classes
        if maze_file:
            self.load(maze_file)

    def _elem_repr(self,elem):
        if self.robot.pos.elem == elem:
            return str(self.robot)
        return str(elem)

    def elem(self,row,col):
        return self._elems[row][col]

    def _row_repr(self, row):
        return ''.join([self._elem_repr(e) for e in row])

    def __repr__(self):
        return '\n'.join([self._row_repr(row) for row in self._elems])

    def _load_elem(self, char, row, col):
        if self._char_classes[char] == Robot:
            elem = Free()
            self.robot = Robot(Position(self, row, col, elem))
            return elem
        return self._char_classes[char]()

    def _load_line(self, line, row):
        return [self._load_elem(char, row, col)
                for col,char in enumerate(line)
                if char != "\n"]

    def load(self, maze_file):
        with open(maze_file, "r") as f:
            self._elems= [self._load_line(line, row)
                          for row,line in enumerate(f)]
