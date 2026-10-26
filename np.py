import  numpy as np

mat = np.arange(1,10).reshape(3,3)
print(mat)

a = np.array([
    [1,2],
    [3,4]
])
b = np.array([12,-3])
solution = np.linalg.solve(a, b)
x , y = solution
print(f" x = {x} , y = {y}")

