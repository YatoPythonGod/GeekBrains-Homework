class Matrix:
    def __init__(self, lst):
        self.lst = lst

    def __str__(self):
        msg = (' '.join(map(str, el)) for el in self.lst)
        return '\n'.join(msg)

    def __add__(self, other):
        return Matrix([self.lst[i][j] + other.lst[i][j] for j in range(len(self.lst[i]))] for i in range(len(self.lst)))


my_lst_1 = [[1, 1, 1], [2, 2, 2], [-1, -1, -1]]
my_lst_2 = [[4, 4, 4], [3, 3, 3], [6, 6, 6]]

a = Matrix(my_lst_1)
b = Matrix(my_lst_2)
print(a + b)
