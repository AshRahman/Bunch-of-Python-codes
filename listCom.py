matrix_2d=[[1,2,3],
           [4,5,6]]

matrix_1d=[num**3 for row in matrix_2d for num in row]
print(matrix_1d)