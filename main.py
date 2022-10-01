def create_matrix(string_count, column_count):
    return [[0] * column_count for i in range(string_count)]


def create_filled_matrix(values, string_count, column_count):
    if len(values) != string_count * column_count:
        raise AttributeError()

    matrix = create_matrix(string_count, column_count)
    for n in range(string_count):
        for m in range(column_count):
            matrix[n][m] = values[n * column_count + m]

    return matrix


def get_minor(matrix, n, m):
    result = create_matrix(3, 3)
    for i in range(3):
        for j in range(3):
            result[i][j] = matrix[i][j]

    del result[n]
    for row in result:
        del row[m]
    return result


def has_notnull_2x2minor(matrix):
    for i in range(3):
        for j in range(3):
            if get_minor(matrix, i, j) != 0:
                return True
    return False


def det2x2(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def det3x3(matrix):
    return matrix[0][0] * matrix[1][1] * matrix[2][2] + matrix[2][0] * matrix[0][1] * matrix[1][2] +\
           matrix[0][2] * matrix[1][0] * matrix[2][1] - matrix[0][2] * matrix[1][1] * matrix[2][0] -\
           matrix[0][0] * matrix[2][1] * matrix[1][2] - matrix[1][0] * matrix[0][1] * matrix[2][2]


# Транспонирование матрицы (возможные размеры матриц: 1х2, 2х1, 1х3, 3х1, 2х2, 3х3).
def transpose(matrix):
    transposed_matrix = create_matrix(len(matrix[0]), len(matrix))
    for n in range(len(matrix)):
        for m in range(len(matrix[0])):
            transposed_matrix[m][n] = matrix[n][m]
    matrix = transposed_matrix
    return matrix


# Умножение матриц (возможные размеры матриц: 1х2, 2х1, 1х3, 3х1, 2х2, 3х3).
def multiply_matrix(first_matrix, second_matrix):
    result_matrix = create_matrix(len(first_matrix), len(second_matrix[0]))
    for i in range(len(first_matrix)):
        for j in range(len(second_matrix[0])):
            for k in range(len(first_matrix[0])):
                result_matrix[i][j] += first_matrix[i][k] * second_matrix[k][j]
    return result_matrix


# Определение ранга матрицы
def calculate_2x2matrix_rang(matrix):
    result = 0
    if map(sum, matrix) != 0:
        result = 1
    if det2x2(matrix) != 0:
        result = 2
    return result


def calculate_3x3matrix_rang(matrix):
    result = 0

    if any(matrix) != 0:
        result = 1
    if has_notnull_2x2minor(matrix):
        result = 2
    if det3x3(matrix) != 0:
        result = 3
    return result


def create_user_matrix():
    strings = int(input("Количесвто строк: "))
    columns = int(input("Количество столбцов: "))
    values = [int(input(">")) for i in range(strings * columns)]
    return create_filled_matrix(values, strings, columns)


action = int(input("Действие; 1. Транспонировать 2. Умножить 3. Ранг: "))

if action == 1:
    m = create_user_matrix()
    print(transpose(m))
elif action == 2:
    m1 = create_user_matrix()
    m2 = create_user_matrix()
    print(multiply_matrix(m1, m2))
elif action == 3:
    m = create_user_matrix()
    print(calculate_2x2matrix_rang(m) if len(m) == 2 else calculate_3x3matrix_rang(m))


