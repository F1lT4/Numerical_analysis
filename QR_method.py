from math import sqrt
from matrix import Matrix
"""Householder method helps to make a diagonal matrix 
which in turn will helps the factor a matrix to an orthogonal (Q) and 
  a diagonal (R) matrix"""


def householder(vector, k_p):  # k_p is the number you want to be 0 in a matrix column
    if not isinstance(vector, Matrix):
        return " not a matrix"
    dim = vector.m_dimensions_test()
    if k_p > dim[0] or k_p < 0:
        print("k_p has a false value")
    elif dim[1] > 1:
        print("not a vector input")
    else:
        u_list = []
        s_start = 0
        for i in range(k_p-1, dim[0]):
            s_start += vector.matrix[i][0] ** 2
        s_en = sqrt(s_start)
        den_om = sqrt(2 * s_en * (s_en + abs(vector.matrix[k_p-1][0])))
        sgn = vector.matrix[k_p-1][0] / abs(vector.matrix[k_p-1][0])
        for j in range(dim[0]):
            if j < k_p - 1:
                u_list.append([0])
            elif j == k_p - 1:
                u_list.append([vector.matrix[j][0] + sgn * s_en])
            else:
                u_list.append([vector.matrix[j][0]])
        u_vector = Matrix(u_list)
        u_vector = u_vector * (1 / den_om)
        i_matrix = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        h_matrix = i_matrix - u_vector * u_vector.transverse() * 2
        return h_matrix


def factors(m_matrix):
    if not isinstance(m_matrix, Matrix):
        return " not a matrix"
    else:
        dim = m_matrix.m_dimensions_test()
        r_matrix = m_matrix
        q_matrix = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        for j in range(dim[1]-1):
            u_list = []
            for i in range(dim[0]):
                u_list.append([r_matrix.matrix[i][j]])
            u_vector = Matrix(u_list)
            h_matrix = householder(u_vector, j+1)
            r_matrix = h_matrix * r_matrix
            q_matrix = q_matrix * h_matrix

        return q_matrix, r_matrix


a_matrix = Matrix([[10, 9, 18], [20, -15, -15], [20, -12, 51]])
print(factors(a_matrix)[0])
print(factors(a_matrix)[1])
moo_matrix = Matrix([[7], [4], [3]])
h_mat = householder(moo_matrix, 1)
print(h_mat * moo_matrix)
