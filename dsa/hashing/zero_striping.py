def zero_stripping(matrix: list[list[int]]) -> list[list[int]]:
    zero_rows = set()
    zero_cols = set()
    if not matrix or not matrix[0]:
        return matrix
    m, n = len(matrix), len(matrix[0])
    for r in range(m):
        for c in range(n):
            if matrix[r][c] == 0:
                zero_rows.add(r)
                zero_cols.add(c)
    for r in range(m):
        for c in range(n):
            if r in zero_rows or c in zero_cols:
                matrix[r][c] = 0
    return matrix
