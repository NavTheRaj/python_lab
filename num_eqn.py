import numpy as np
#CREATING THE MATRIX A
mat_A=np.array([[1,1,1],[3,4,7],[5,10,4]])
mat_B=np.array([10,7,6])

x_by_mat=0
x_by_solve=0


#FINDING X BY MATRIX METHOD
x_by_mat=np.linalg.inv(mat_A).dot(mat_B)

print(x_by_mat)

#FINDING X BY SOLVE METHOD
x_by_solve=np.linalg.solve(mat_A,mat_B)

print(x_by_solve)
