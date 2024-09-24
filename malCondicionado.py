import numpy as np

A = np.array([[2.0001,2.0002,2.0003],
              [2.0000,2.0000,2.0000],
              [2.0002,2.0001,2.0000]])

B = np.array([2.0006, 1.0000, 1.0003])

invA = np.linalg.inv(A)
detA = np.linalg.det(A)
condA = np.linalg.cond(A)
identA = np.dot(A, invA)

print(f'Determinante de la matriz: \n {detA}')
print(f'Matriz identidad: \n {identA}')
print(f'Condicional de la matriz: \n {condA}')

print(f"""NOTA: La matriz identidad calculada por python difiere de la calculada
por octave""")