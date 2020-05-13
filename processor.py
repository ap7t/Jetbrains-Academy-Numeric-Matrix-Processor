class MatrixException(Exception):
    pass

class Matrix:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.rows = []

    @classmethod
    def create(cls):
        """
            Create matrix by reading input from stdin
        """
        n, m = list(map(int, input().split()))
        mat = Matrix(n, m)
        for _ in range(mat.n):
            row = list(map(int, input().split()))
            mat.rows.append(row)

        return mat

    def __str__(self):
        """
            Return string representation of matrix
        """
        outstr = ""
        for row in self.rows:
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
            mat = Matrix(self.n, self.m)
            for r in range(self.n):
                row = list(map(sum, zip(self.rows[r], other.rows[r])))
                mat.rows.append(row)
            return mat
