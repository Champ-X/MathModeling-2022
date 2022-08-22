import numpy as np


a = np.array([0, 3, 1, 6, 5, 2, 4, 7])
print(a)
print(a[a])
a[a] = np.arange(8)
print(a)

b = np.array([[1, 2], [3, 4], [5, 6]])
num = np.array([1, 0, 2])
print(b[num, 0])
print(b[num, 1])

''' output
[0 1 2 3 4 5 6 7]
[0 3 1 6 5 2 4 7]

[0 2 5 1 6 4 3 7]

[3 1 5]
[4 2 6]
'''