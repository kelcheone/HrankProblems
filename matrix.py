def add_matrix(m1, m2):
    """Add two matrices of the same size"""
    if len(m1) != len(m2):
        raise ValueError("Matrices must be the same size")
    result = []
    for i in range(len(m1)):
        row = []
        for j in range(len(m1[i])):
            row.append(m1[i][j] + m2[i][j])
        result.append(row)
    return result


m1 = [[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]]
m2 = [[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]]

# print(add_matrix(m1, m2))

# get diagonal of matrix


def get_diagonal(m):
    """Get the diagonal of a matrix"""
    result = []
    for i in range(len(m)):
        result.append(m[i][i])
    sum = 0
    for num in result:
        sum += num
    return sum


print(get_diagonal(m1))


def get_right_diagonal(m):
    """Get the right diagonal of a matrix"""
    result = []
    for i in range(len(m)):
        result.append(m[i][len(m) - 1 - i])
    sum = 0
    for num in result:
        sum += num
    return sum


print(get_right_diagonal(m1))


def diagonalDifference(arr):
    # Write your code here
    lresult = []
    rresult = []
    for i in range(len(arr)):
        lresult.append(arr[i][i])
    for i in range(len(arr)):
        rresult.append(arr[i][len(arr) - 1 - i])
    # add all in the array
    lsum = 0
    rsum = 0
    for num in lresult:
        lsum += num
    for num in rresult:
        rsum += num
    if lsum > rsum:
        return lsum - rsum
    else:
        return rsum - lsum


print("____________________________")

print(diagonalDifference(m1))
