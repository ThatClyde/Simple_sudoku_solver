
from itertools import chain
from textwrap import dedent


class Table:
    template = dedent(
        """
        +-------------------------------------+
        | {} | {} | {} || {} | {} | {} || {} | {} | {} |
        |---+---+---++---+---+---++---+---+---|
        | {} | {} | {} || {} | {} | {} || {} | {} | {} |
        |---+---+---++---+---+---++---+---+---|
        | {} | {} | {} || {} | {} | {} || {} | {} | {} |
        |===+===+===++===+===+===++===+===+===|
        | {} | {} | {} || {} | {} | {} || {} | {} | {} |
        |---+---+---++---+---+---++---+---+---|
        | {} | {} | {} || {} | {} | {} || {} | {} | {} |
        |---+---+---++---+---+---++---+---+---|
        | {} | {} | {} || {} | {} | {} || {} | {} | {} |
        |===+===+===++===+===+===++===+===+===|
        | {} | {} | {} || {} | {} | {} || {} | {} | {} |
        |---+---+---++---+---+---++---+---+---|
        | {} | {} | {} || {} | {} | {} || {} | {} | {} |
        |---+---+---++---+---+---++---+---+---|
        | {} | {} | {} || {} | {} | {} || {} | {} | {} |
        +-------------------------------------+
        """
    )
    
    def __init__(self):
        self.table = []
        for i in range(9):
            self.table.append([0,0,0, 0,0,0, 0,0,0])
        self.flagged_spots = 0
        self.flag_num = 0
        self.flag_row = 0
        self.flag_column = 0

    
    def __str__(self):
         return self.template.format(*chain.from_iterable(self.table))
    
    def iter_sector(self, id):
        """
        This will provide an iterator for the sector given by id.

        Sector map:
             0 1 2 3 4 5 6 7 8
            +-----------------+
          0 |     |     |     |
          1 |  0  |  1  |  2  |
          2 |     |     |     |
            +-----+-----+-----+
          3 |     |     |     |
          4 |  3  |  4  |  5  |
          5 |     |     |     |
            +-----+-----+-----+
          6 |     |     |     |
          7 |  6  |  7  |  8  |
          8 |     |     |     |
            +-----+-----+-----+
        Args:
            id (int): the id of the sector

        Returns:
            a tuple of (the number in the block, row id, column id)
        """
        # hard coded because I suck at math.
        # this is a map of sector id to tuples of points: 
        # (starting row, starting column), (ending row, ending column)
        # where the end values are inclusive.
        sector_map = {
            0: ((0, 0), (2, 2)),
            1: ((3, 0), (5, 2)),
            2: ((6, 0), (8, 2)),
            3: ((0, 3), (2, 5)),
            4: ((3, 3), (5, 5)),
            5: ((6, 3), (8, 5)),
            6: ((0, 6), (6, 8)),
            7: ((3, 6), (5, 8)),
            8: ((6, 6), (8, 8)),
        }

        sector = sector_map.get(id)
        if not sector:
            raise Exception('Invalid sector ID: {}'.format(id))
        (start_col, start_row), (end_col, end_row) = sector
        for row in range(start_row, end_row + 1):
            for col in range(start_col, end_col + 1):
                yield self.table[row][col], row, col
               
    # determining if the number is already in the current 9x9 sector
    def num_is_not_in_sector(self, check_row, check_col, num):
        sector_flag = True
        if check_row < 3:
            row_sector = (0,1,2)
        elif 3 <= check_row <= 5: 
            row_sector = (3,4,5)
        elif check_row >= 6:
            row_sector = (6,7,8)
        if check_col < 3:
            col_sector = (0,1,2)
        elif 3 <= check_col <= 5: 
            col_sector = (3,4,5)
        elif check_col >= 6:
            col_sector = (6,7,8)
        for i in (row_sector):
            for j in (col_sector):
                if num == self.table[i][j]:
                    return False
        return sector_flag

    def current_box_is_blank(self, check_row, check_col):
        if self.table[check_row][check_col] == 0:
            return True
        else:
            return False
    
    def puzzle_has_blanks(self):
        for i in range(9):
            for j in range(9):
                if self.table[i][j] == 0:
                    return True
        return False
        
    def num_is_not_in_row(self, row, col, num):
        row_flag = False
        for i in range(9):
            if (self.table[row][i] == num) and (i != col):
                return False
            else:
                row_flag = True
        return row_flag
        
    def num_is_not_in_col(self, row, col, num):
        col_flag = False
        for i in range(9):
            if (self.table[i][col] == num) and (i != row):
                return False
            else:
                col_flag = True
        return col_flag
        
    def get_table(self):
        
        # During testing, this'll speed the process update
        """
        self.table = [[6,0,0, 1,0,8, 2,0,3],
                    [0,2,0, 0,4,0, 0,9,0],
                    [8,0,3, 0,0,5, 4,0,1],
                    [5,0,4, 6,0,7, 0,0,9],
                    [0,3,0, 0,0,0, 0,5,0],
                    [7,0,0, 8,0,3, 1,0,2],
                    [0,0,1, 7,0,0, 9,0,6],
                    [0,8,0, 0,3,0, 0,2,0],
                    [3,0,2, 9,0,4, 0,0,5]]
        """
    
        row = 0
        while row < 9:
            sudoku_row = input("Please enter the contents of row {}, using 0 to represent blanks:".format(row+1))
            if len(sudoku_row) == 9:
                column = 0
                while column < 9:
                    number_in_box = int(sudoku_row[column])
                    self.table[row][column] = number_in_box
                    column += 1
                row += 1
            else:
                print("You can only enter 9 numbers. Not letters. Not more. Not fewer. 9 numbers.")
     


        
