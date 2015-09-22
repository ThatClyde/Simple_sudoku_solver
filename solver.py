from models import Table
from utils import clearscreen

# start with blank screen
clearscreen()
# building the blank sudoku table
sudoku = Table()
# Having the user enter the sudoku puzzle
sudoku.get_table()

print("This is your sudoku puzzle:")
print(sudoku)
num = 1
row = 0
col = 0
counter = 0
max_tries = 1000
# This will loop through while the puzzle isn't solved, or until it's
# reached the maximum tries.
while sudoku.puzzle_has_blanks() and counter < max_tries:
    for num in range(10):
        # this will cause it to iterate through the sectors in the grid
        for sector_id in range(9):
            # setting the number of flagged/possible spots to 0
            sudoku.flagged_spots = 0
            # the massive if statements that looks at a box in the puzzle to
            # determine if those things are all true.
            for number_in_block, row, col in sudoku.iter_sector(sector_id):
                if (sudoku.current_box_is_blank(row, col)
                        and sudoku.num_is_not_in_sector(row, col, num)
                        and sudoku.num_is_not_in_row(row, col, num)
                        and sudoku.num_is_not_in_col(row, col, num)):
                    # if all are true, it flags that spot as a possible
                    # solution, and records it.
                    sudoku.flagged_spots += 1
                    sudoku.flag_num = num
                    sudoku.flag_row = row
                    sudoku.flag_col = col
                    number_that_was_in_block = number_in_block
                    # print("I'm flagging {},{}, for number: {} which is in sector {}, and this is the {} flag.".format(row,col,num,sector_id,sudoku.flagged_spots))
            # prior to going to the next number, if only one flag has been
            # created in the section, the spot must be good, so it updates the
            # table.
            if sudoku.flagged_spots == 1:
                sudoku.table[
                    sudoku.flag_row][
                    sudoku.flag_col] = sudoku.flag_num
                print("Putting {} in sector {} at {} row {} col.".format(
                    num, sector_id + 1, sudoku.flag_row + 1, sudoku.flag_col + 1))

    counter += 1


if counter == max_tries:
    print("The solver took {} passes at it, and this is the best if could do:".format(counter))
else:
    print("Here is your solved puzzle! It took {} passes.".format(counter))
print(sudoku)
