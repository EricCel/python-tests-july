#Design a 3 x 3 matrix using nested lists and implement the sum of its main diagonal.

matrix = [[1,2,3],[4,5,6],[7,8,9]]

def dSUM(matrix):
    if all([True if len(matrix[i]) == len(matrix[i - 1]) else False for i in range(len(matrix))]):
        return sum([matrix[i][i] for i in range(len(matrix))])
    else:
        return "Error, size must match"

print(dSUM(matrix))