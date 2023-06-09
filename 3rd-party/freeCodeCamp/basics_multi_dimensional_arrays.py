import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = np.zeros((3, 3))
c = np.ones((3, 3))
d = np.full((3, 3), 7)
e = np.eye(3)
f = np.random.random((3, 3))
g = np.random.randint(0, 10, (3, 3))
h = np.random.randn(3, 3)
print("np.array \n\n", a, end="\n\n")
print("np.zeros \n\n",b, end="\n\n")
print("np.ones \n\n",c, end="\n\n")
print("np.full \n\n",d, end="\n\n")
print("np.eye \n\n",e, end="\n\n")
print("np.array.random.random \n\n",f, end="\n\n")
print("np.array,random.randint \n\n",g, end="\n\n")
print("np.array.random.randn \n\n",h, end="\n\n")