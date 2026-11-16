def verify_sudoku_board(board: list[list[int]]) -> bool:
    row_sets = [set() for _ in range(9)]
    column_sets = [set() for _ in range(9)]
    subgrid_sets = [[set() for _ in range(3)] for _ in range(3)]
    for row in range(9):
        for column in range(9):
            number = board[row][column]
            if number == 0:
                continue
            if number in row_sets[row]:
                return False
            if number in column_sets[column]:
                return False
            if number in subgrid_sets[row // 3][column // 3]:
                return False
            row_sets[row].add(number)
            column_sets[column].add(number)
            subgrid_sets[row // 3][column // 3].add(number)
    return True


