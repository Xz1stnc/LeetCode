def lucky_number(matrix: list[list[int]]) -> list[int]:
    row_min = [min(row) for row in matrix]
    col_max = [max(col) for col in zip(*matrix)]
    lucky = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == row_min[i] and matrix[i][j] == col_max[j]:
                lucky.append(matrix[i][j])
    return lucky


a = lucky_number([[1, 10, 4, 2, 5], [9, 3, 8, 7, 6], [15, 16, 17, 12, 14]])
print(a)
