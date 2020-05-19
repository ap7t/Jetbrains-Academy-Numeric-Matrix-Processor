class Matrix:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.matrix = [[0] * m for _ in range(n)]

    @classmethod
    def create(cls):
        """
            Create matrix by reading input from stdin
        """
        n, m = list(map(int, input("Enter size of matrix: ").split()))
        mat = Matrix(n, m)
        print("Enter matrix: ")
        for i in range(mat.n):
            row = list(map(float, input().split()))
            mat.matrix[i] = row
        return mat

    def __str__(self):
        """
            Return string representation of matrix
        """
        outstr = ""
        for row in self.matrix:
            outstr += " ".join(map(str, row)) + '\n'
        return outstr

    def __add__(self, other):
        """
            Overload the add operator to add two matrices
            Returns a new instance of Matrix
        """
        if self.m != other.m and self.n != other.n:
            raise MatrixException
        else:
            new_mat = Matrix(self.n, self.m)
            for r in range(self.n):
                row = list(map(sum, zip(self.matrix[r], other.matrix[r])))
                new_mat.matrix[r] = row
            return new_mat

    def __mul__(self, other):
        """
            Override the multiplication operator
            Returns product as new instance of matrix class
        """
        if not isinstance(other, Matrix):
            new_mat = Matrix(self.n, self.m)
            for i in range(len(self.matrix)):
                new_mat.matrix[i] = list(map(lambda x: x * other, self.matrix[i]))
            return new_mat
        else:
            if self.m != other.n:
                raise MatrixException
            else:
                new_mat = Matrix(self.n, other.m)
                for i in range(new_mat.n):
                    for j in range(new_mat.m):
                        for k in range(other.n):
                            new_mat.matrix[i][j] += self.matrix[i][k] * other.matrix[k][j]
                return new_mat

class MatrixException(Exception):
    pass


"""
11*11 + 12*21 + 13*31 |  11*12 + 12*22 + 13*32 | 11*13 + 12*23 + 13*33
21*11 + 22*21 + 23*31 |  21*12 + 22*22 + 23*32 | 21*13 + 22*23 + 23*33
31*11 + 32*21 + 33*31 |  31*12 + 32*22 + 33*32 | 31*13 + 32*23 + 33*33
"""
