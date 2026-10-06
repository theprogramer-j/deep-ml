def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
    if len(a[0]) != len(b):
        return -1
    return [[sum([a[row][i]*b[i][col] for i in range(len(b))]) for col in range(len(b[0]))] for row in range(len(a))]