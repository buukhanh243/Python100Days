matrix = [[1, 2, 3],
           [4, 5, 6],
           [7, 10, 11]]

# for row in range(len(matrix)):
#     for col in range(len(matrix)):
#         print(matrix[row][col])

list_converted = [matrix[row][col] for row in range(len(matrix)) for col in range(len(matrix))]
print(list_converted)

print([x for x in zip(*matrix)])