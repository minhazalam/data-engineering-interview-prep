from dsa.hashing.verify_sudoku_board import verify_sudoku_board


def make_empty_board():
    return [[0 for _ in range(9)] for _ in range(9)]


def test_valid_board():
    board = make_empty_board()
    board[0][0:3] = [1, 2, 3]
    board[1][0:3] = [4, 5, 6]
    board[2][0:3] = [7, 8, 9]

    assert verify_sudoku_board(board) is True


def test_duplicate_in_row():
    board = make_empty_board()
    board[0][0] = 5
    board[0][1] = 5

    assert verify_sudoku_board(board) is False


def test_duplicate_in_column():
    board = make_empty_board()
    board[0][0] = 5
    board[1][0] = 5

    assert verify_sudoku_board(board) is False


def test_duplicate_in_subgrid():
    board = make_empty_board()
    board[0][0] = 5
    board[1][1] = 5

    assert verify_sudoku_board(board) is False


def test_multiple_empty_cells():
    board = make_empty_board()

    assert verify_sudoku_board(board) is True
