import random
from lld.snake_and_ladder.cell import Cell
from lld.snake_and_ladder.jump import Jump


class Board:
    def __init__(self, size, count_snake, count_ladder):
        self.cells = [[None for i in range(size)] for i in range(size)]
        self.size = size
        self.count_snake = count_snake
        self.count_ladder = count_ladder
        self.initialise_cells()
        self.add_snake_and_ladder()

    def initialise_cells(self):
        for i in range(self.size):
            for j in range(self.size):
                self.cells[i][j] = Cell()

    def add_snake_and_ladder(self):
        already_used_cells = set()
        while self.count_snake > 0:
            start = random.randint(1, self.size * self.size)
            end = random.randint(1, self.size * self.size)
            if end >= start or end in already_used_cells or start in already_used_cells:
                continue
            cell = self.get_cell(start)
            cell.jump = Jump(type="snake_bite", start=start, end=end)
            already_used_cells.add(start)
            already_used_cells.add(end)
            self.count_snake -= 1
        while self.count_ladder > 0:
            start = random.randint(1, self.size * self.size)
            end = random.randint(1, self.size * self.size)
            if end <= start or end in already_used_cells or start in already_used_cells:
                continue
            cell = self.get_cell(start)
            cell.jump = Jump(type="ladder", start=start, end=end)
            already_used_cells.add(start)
            already_used_cells.add(end)
            self.count_ladder -= 1

    def get_cell(self, position):
        """
        :rtype: Cell
        """
        return self.cells[int(position/self.size)][int(position % self.size)]


# board = Board(10, count_snake=2, count_ladder=2)
# print(board)