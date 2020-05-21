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

    def transpose_diagonal(self):
        new_mat = Matrix(self.m, self.n)
        for j in range(self.m):
            new_row = []
            for i in range(self.n):
                new_row.append(self.matrix[i][j])
            new_mat.matrix[j] = new_row

        return new_mat

    def transpose_side_diagonal(self):
        new_mat = Matrix(self.m, self.n)
        for j in range(self.m -1, -1, -1):
            new_row = []
            for i in range(self.n - 1, -1, -1):
                new_row.append(self.matrix[i][j])
            new_mat.matrix[self.n-1 - j] = new_row

        return new_mat

    def transpose_vertical(self):
        new_mat = Matrix(self.n, self.m)
        for i in range(len(self.matrix)):
            new_mat.matrix[i] = reversed(self.matrix[i])
        return new_mat

    def transpose_horizontal(self):
        new_mat = self
        size = new_mat.n - 1
        i = 0
        while i <= size // 2:
            new_mat.matrix[i], new_mat.matrix[size-i] = new_mat.matrix[size-i], new_mat.matrix[i]
            i += 1
        return new_mat


class MatrixException(Exception):
    pass

if __name__ == '__main__':
    m = Matrix.create()
    print("Original matrix:")
    print(m)
    mT = m.transpose_side_diagonal()
    print("Transposed matrix")
    print(mT)