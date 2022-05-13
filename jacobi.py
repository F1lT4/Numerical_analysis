from matrix import Matrix
""" first make the system of linear equations into a matrix and a vector
example:
    3x + 2y = 19
    4x + 10y = 10
    M+N = [[3, 2], [4, 10]] 
    b = [[19], [10]]
    this method skips the trouble of reversing the matrix
"""


def jacobi(m_and_n, vector, rev=6):  # M+N, b
    dim = m_and_n.m_dimensions_test()
    n_list = []
    for j in range(dim[0]):
        n_list.append(m_and_n.matrix[j][:])
    n_matrix = Matrix(n_list)
    for i in range(dim[0]):  # the matrix without the diagonal
        n_matrix.matrix[i][i] = 0
    m_matrix = m_and_n - n_matrix  # only the diagonal matrix
    det_m = 1
    for j in range(dim[0]):
        det_m *= m_matrix.matrix[j][j]
    inv_list = []
    for z in range(dim[0]):
        inv_list.append(m_matrix.matrix[z][:])
    m_inverse = Matrix(inv_list)
    k = 0
    for z in range(dim[0]):  # inverse the M matrix
        m_inverse.matrix[k][k] = m_matrix.matrix[dim[0]-1-k][dim[0]-1-k] / det_m
        k += 1
    x_list = []
    for i in range(dim[0]):  # this is for the starting vector
        x_list.append([0])   # you can make it something other than 0
    x_vector = Matrix(x_list)
    # start of the function
    for _ in range(rev):
        x_vector = m_inverse * n_matrix * x_vector * (-1) + m_inverse * vector

    return x_vector


""" Lets say we have the following system:
    5x - y = 3
    -1x +10y = 19
"""

mn_matrix = Matrix([[5, -1], [-1, 10]])
b_vector = Matrix([[3], [19]])
print(jacobi(mn_matrix, b_vector))
