from matrix import Matrix

"""dynamic method to compute eigenvalues and vectors,
finds the vector for the biggest eigenvalue,
doesn't always work"""


def dyn_l(mat, accuracy=0.001):
    if isinstance(mat, Matrix) and mat.m_dimensions_test() is not None:  # only for the class matrix
        dim = mat.m_dimensions_test()
        vec_1 = []
        for i in range(dim[0]):  # first vector is the front elements of the matrix (for convenience)
            vec_1.append([mat.matrix[0][i]])
        vector_1 = Matrix(vec_1)
        k = 0  # number of iterations
        u_list = []  # list of vectors
        while True:
            u_vec = mat * vector_1
            vector_1 = u_vec * (1 / u_vec.matrix[0][0])
            u_list.append(u_vec)
            if k >= 1:  # in order to have at least two vectors to compare
                # check the difference between the first element of the two vectors
                if abs(u_list[k].matrix[0][0] - u_list[k-1].matrix[0][0]) < accuracy:
                    return vector_1, u_vec  # returns tuple of two matrix elements
            k += 1
    else:
        print("not a matrix")
        return


# example 1
matrix_1 = Matrix([[2, 1], [1, 2]])
print(f"{dyn_l(matrix_1)[0]} \n {dyn_l(matrix_1)[1]} "
      f" \n λ = {dyn_l(matrix_1)[1].matrix[0][0] / dyn_l(matrix_1)[0].matrix[0][0]}")
# example 2
matrix_2 = Matrix([[24, -1, 15], [9, -2, 5], [-1, 3, 5]])
print(f"{dyn_l(matrix_2)[0]} \n {dyn_l(matrix_2)[1]} "
      f"\n λ = {dyn_l(matrix_2)[1].matrix[0][0] /dyn_l(matrix_2)[0].matrix[0][0]}")
