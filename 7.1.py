class Matrix:
    def __init__(self, elems):
        self.elems = elems

    def __str__(self):
        return '\n'.join('\t'.join(str(el) for el in elem) for elem in self.elems)

    def __add__(self, other):
        # for elem, new_elem in self.elems, other.elems:
        mat = [[str(int(self.elems[i][j]) + int(other.elems[i][j])) for j in range(len(self.elems[i]))] for i in range(len(self.elems))]
        return Matrix(mat)


matr_1 = Matrix([[5, 6], [1, 2]])
matr_2 = Matrix([[1, 2], [2, 1]])
print(matr_1)
print(matr_1.__add__(matr_2))
