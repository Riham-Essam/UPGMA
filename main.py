def prepare_table(start, end):
    labels = []
    for i in range(ord(start), ord(end)+1):
        labels.append(chr(i))
    return labels
matrix_labels = prepare_table("A", "E")
matrix = [
    #A(0)  #B(1)  #C(2)  #D(3)  #E(4)               x:vertical(col)/y:horizontal(row)
    [],                               #A(0)
    [20],                             #B(1)
    [60, 50],                         #C(2)
    [100, 90, 40],                    #D(3)
    [90, 80, 50, 30],                 #E(4)
    ]

def select_smallest_cell(matrix):
    min_cell = float("inf")
    x, y = -1, -1
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] < min_cell:
                min_cell = matrix[i][j]
                x, y = j, i
    return x, y

def merge_cells(matrix, x, y):
    # combine values of rows of 2 selected labels
    row = []
    for i in range(0, x):
        row.append((matrix[x][i] + matrix[y][i]) / 2)
    matrix[x] = row
    # combine values of columns of 2 selected labels
    for i in range(y + 1, len(matrix)):
        matrix[i][x] = (matrix[i][x] + matrix[i][y]) / 2
        # Remove unneeded col
        del matrix[i][y]
    # Remove unneeded row
    del matrix[y]

def merge_cell_labels(labels, x, y):
    labels[x] = "(" + labels[x] + "," + labels[y] + ")"
    del labels[y]

def UPGMA(matrix, labels):
    while len(labels) > 1:
        x, y = select_smallest_cell(matrix)
        merge_cells(matrix, x, y)
        merge_cell_labels(labels, x, y)
        print(labels)
    return labels[0]

#our main..
tree_output = UPGMA(matrix, matrix_labels)
print("Final Result:")
print(tree_output)
