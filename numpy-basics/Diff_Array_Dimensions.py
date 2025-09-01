import numpy as np

#Creating a 1-D array
arr_1d = np.array([1,2,3,4])
print(arr_1d)
print("Array Dimension: ",arr_1d.ndim)
print('================================')

#Creating a 2-D array
arr_2d = np.array([[1,2],[3,4]])
print(arr_2d)
print("Array Dimension: ",arr_2d.ndim)
print('================================')

#Creating a 3-D array
arr_3d = np.array([[[1,2],[3,4],[5,6]]])
print(arr_3d)
print("Array Dimension: ",arr_3d.ndim)
print('================================')

#Creating a n-D array
arr_nd = np.array([1,2],ndmin=5)
print(arr_nd)
print("Array Dimension: ",arr_nd.ndim)
print('================================')