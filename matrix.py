class Matrix:
    def __init__(self, matrix):
        try:
            if isinstance(matrix, list):  # input can only be a list
                width = len(matrix)
                num_floats = 0
                for element in matrix:
                    if isinstance(element, (float, int)):  # elements can only be numerical
                        num_floats += 1
                if width == num_floats:
                    self.matrix = [matrix]
                else:
                    self.matrix = matrix
            else:
                raise ValueError("This is not a matrix")
        except ValueError:
            print("This is not a matrix please redefine it!")
            self.matrix = []  # false input returns an empty matrix

    def m_redefine(self, new_matrix):  # used when the input was wrong
        try:
            if isinstance(new_matrix, list):
                self.matrix = new_matrix
            else:
                raise ValueError("This is not a matrix")
        except ValueError:
            print("This is not a matrix please redefine it!")

    def m_dimensions_test(self):  # returns matrix dimensions (r, c) or None
        width = len(self.matrix)
        num_floats = 0
        num_matrix = 0
        for element in self.matrix:
            if isinstance(element, (float, int)):
                num_floats += 1
            elif isinstance(element, list):
                num_matrix += 1
            else:
                print("there is a problem with the matrix elements")
                return
        if width == 1:
            if isinstance(self.matrix, list):
                inner_width = len(self.matrix[0])
                inner_floats = 0
                for element in self.matrix[0]:
                    if isinstance(element, (float, int)):
                        inner_floats += 1
                if inner_width == inner_floats != 0:
                    dim = (1, inner_width)
                    return dim
                else:
                    print("there is a problem with the matrix elements")
                    return

        if (len(self.matrix) != num_matrix != 0) or (len(self.matrix) != num_floats != 0):
            print("the matrix is uneven")
            return
        elif num_floats == len(self.matrix):
            dim = (1, width)
            return dim
        elif num_matrix == len(self.matrix):
            for i in range(len(self.matrix)-1):
                if len(self.matrix[i]) != len(self.matrix[i+1]):
                    print("the matrix is uneven")
                    return
            dim = (width, len(self.matrix[0]))
            return dim  # the tuple it returns is : (rows, columns)

    def transverse(self):  # simply makes the rows into columns
        dim = self.m_dimensions_test()
        new_matrix = []
        if dim is None:
            print("this matrix is not transversable")
            return Matrix([])
        elif dim[0] == 1:
            for el in self.matrix[0]:
                new_matrix.append([el])
            return Matrix(new_matrix)
        else:
            for i in range(dim[1]):
                new_matrix.append([])
            for z in range(dim[0]):
                for j in range(dim[1]):
                    new_matrix[j].append(self.matrix[z][j])

            return Matrix(new_matrix)

    def trace(self):
        dim = self.m_dimensions_test()
        if dim is None:
            print("Not a matrix")
            return
        if dim[0] == dim[1]:
            trace = 0
            for i in range(dim[0]):
                trace += self.matrix[i][i]
            return trace
        else:
            print("Not a matrix with trace")
            return

    def ii_constant_tensor(self):  # only for 2x2 and 3x3
        # only for tensors
        dim = self.m_dimensions_test()
        if dim is None:
            print("Not a matrix")
            return
        if dim[0] == dim[1] <= 3:
            trace = self.trace()
            square_m = self * self
            duo_con = 0.5 * (trace ** 2 - square_m.trace())
            return duo_con
        else:
            print("Not a matrix with II")
            return

    def det_tensor(self):  # only for 2x2 and 3x3
        dim = self.m_dimensions_test()
        if dim is None:
            print("Not a matrix")
            return
        if dim[0] == dim[1]:
            m_det = 0
            if dim[0] == 2:
                m_det += self.matrix[0][0] * self.matrix[1][1]
                m_det -= self.matrix[0][1] * self.matrix[1][0]
                return m_det
            elif dim[0] == 3:  # a formula that works only for a 3x3 matrix
                trace_m = self.trace()
                square_m = self * self
                cube_m = square_m * self
                m_det = (trace_m**3 - 3*trace_m*square_m.trace() + 2*cube_m.trace())/6
                return m_det
            else:
                print("Not a tensor")
                return
        else:
            print("Not a matrix with det")
            return

    def inverse_tensor(self):  # only for 2x2 and 3x3
        dim = self.m_dimensions_test()
        new_matrix = []
        if dim is None:
            print("This is a false matrix")
            return Matrix([])
        if dim[0] == dim[1]:
            if dim[0] == 2:
                det = self.det_tensor()
                if det > 0:
                    new_matrix.append([self.matrix[1][1], -self.matrix[0][1]])
                    new_matrix.append([-self.matrix[1][0], self.matrix[0][0]])
                    new_mar = Matrix(new_matrix)
                    new_mar = new_mar * (1/det)
                    return new_mar
                else:
                    print("The matrix is not inversable")
                    return Matrix([])
            elif dim[0] == 3:
                det = self.det_tensor()
                if det > 0:
                    new_mat = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                    new_mat[0][0] = (self.matrix[2][2]*self.matrix[1][1] - self.matrix[1][2]*self.matrix[2][1]) / det
                    new_mat[1][1] = (self.matrix[0][0]*self.matrix[2][2] - self.matrix[0][2]*self.matrix[2][0]) / det
                    new_mat[2][2] = (self.matrix[0][0]*self.matrix[1][1] - self.matrix[0][1]*self.matrix[1][0]) / det

                    new_mat[1][0] = (-self.matrix[1][0]*self.matrix[2][2] + self.matrix[1][2]*self.matrix[2][0]) / det
                    new_mat[2][0] = (self.matrix[1][0]*self.matrix[2][1] - self.matrix[1][1]*self.matrix[2][0]) / det
                    new_mat[0][1] = (-self.matrix[0][1]*self.matrix[2][2] + self.matrix[0][2]*self.matrix[2][1]) / det
                    new_mat[2][1] = (-self.matrix[0][0]*self.matrix[2][1] + self.matrix[2][0]*self.matrix[0][1]) / det
                    new_mat[0][2] = (self.matrix[0][1]*self.matrix[1][2] - self.matrix[1][1]*self.matrix[0][2]) / det
                    new_mat[1][2] = (-self.matrix[0][0]*self.matrix[1][2] + self.matrix[0][2]*self.matrix[1][0]) / det
                    n_m = Matrix(new_mat)  # adjugate matrix
                    return n_m

                else:
                    print("The matrix is not inversable")
                    return Matrix([])
            else:
                print("not a tensor")
        else:
            print("The matrix is not inversable")
            return Matrix([])

    def __add__(self, other):
        dim_1 = self.m_dimensions_test()
        dim_2 = other.m_dimensions_test()
        new_matrix = []
        if dim_2 == dim_1 is not None:
            if dim_2[0] == 1:
                for i in range(dim_1[1]):
                    element = self.matrix[0][i] + other.matrix[0][i]
                    new_matrix.append(element)
                return Matrix(new_matrix)
            else:
                for j in range(len(self.matrix)):
                    in_matrix = []
                    for i in range(len(self.matrix[j])):
                        element = self.matrix[j][i] + other.matrix[j][i]
                        in_matrix.append(element)
                    new_matrix.append(in_matrix)
                return Matrix(new_matrix)
        else:
            print("the matrix can not be added")
            return Matrix([])

    def __sub__(self, other):
        dim_1 = self.m_dimensions_test()
        dim_2 = other.m_dimensions_test()
        new_matrix = []
        if dim_2 == dim_1 is not None:
            if dim_2[0] == 1:
                for i in range(dim_1[1]):
                    element = self.matrix[0][i] - other.matrix[0][i]
                    new_matrix.append(element)
                return Matrix(new_matrix)
            else:
                for j in range(len(self.matrix)):
                    in_matrix = []
                    for i in range(len(self.matrix[j])):
                        element = self.matrix[j][i] - other.matrix[j][i]
                        in_matrix.append(element)
                    new_matrix.append(in_matrix)
                return Matrix(new_matrix)
        else:
            print("the matrix can not be added")
            return Matrix([])

    def __mul__(self, other):
        if isinstance(other, Matrix):
            dim_1 = self.m_dimensions_test()
            dim_2 = other.m_dimensions_test()
            new_matrix = []
            if dim_1 is not None and dim_2 is not None:
                if dim_1[1] == dim_2[0]:
                    for i in range(dim_1[0]):
                        in_matrix = []
                        for j in range(dim_2[1]):
                            new_el = 0
                            for z in range(dim_2[0]):
                                element = self.matrix[i][z] * other.matrix[z][j]
                                new_el += element
                            in_matrix.append(new_el)
                        new_matrix.append(in_matrix)
                    return Matrix(new_matrix)
                else:
                    print("the matrix can not be multiplied")
                    return Matrix([])
            else:
                print("the matrix can not be multiplied")
                return Matrix([])
        elif isinstance(other, (int, float)):
            dim_1 = self.m_dimensions_test()
            new_matrix = []
            if dim_1[0] == 1:
                for element in self.matrix:
                    new_el = element * other
                    new_matrix.append(new_el)
                return Matrix(new_matrix)
            elif dim_1 is None:
                print("the matrix can not be multiplied")
                return Matrix([])
            else:
                for i in range(dim_1[0]):
                    in_matrix = []
                    for j in range(dim_1[1]):
                        new_el = other * self.matrix[i][j]
                        in_matrix.append(new_el)
                    new_matrix.append(in_matrix)
                return Matrix(new_matrix)

    def __str__(self):
        st = "_" * 20
        st += "\n"
        dim = self.m_dimensions_test()
        if dim is None:
            return "False, or empty matrix"
        elif dim[0] != 1:
            for element in self.matrix:
                st += "|"
                st += "["
                for el in element:
                    st += str(round(el, 4))
                    st += ","
                st = st[:-1]
                st += "]"
                st += "|"
                st += "\n"
            st += "-" * 20
            return st
        else:
            st += "|"
            st += str(self.matrix)
            st += "|"
            st += "\n"
            st += "-" * 20
            return st

    def __repr__(self):
        st = "_" * 20
        st += "\n"
        dim = self.m_dimensions_test()
        if dim is None:
            return "False, or empty matrix"
        elif dim[0] != 1:
            for element in self.matrix:
                st += "|"
                st += str(element)
                st += "|"
                st += "\n"
            st += "-" * 20
            return st
        else:
            st += "|"
            st += str(self.matrix)
            st += "|"
            st += "\n"
            st += "-" * 20
            return st
