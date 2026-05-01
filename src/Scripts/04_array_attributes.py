import numpy as np

arr = np.array([[1,2,3],[4,5,6],[7,8,'9']]) # 2D array with mixed data types, it will be upcasted to string
print("Array:\n", arr)

# shape of an array
print("Shape of the array:", arr.shape)

# size of an array
print("Size of the array:", arr.size)

# number of dimensions in an array is called its rank
print("Number of dimensions (rank) of the array:", arr.ndim)

# data type of the array
print("Data type of the array:", arr.dtype)  # <U21 string of length 21, because the longest string in the array is '9' which has length 1, but it is upcasted to string so it will be stored as a string of length 21 (default length for string data type in numpy)

# item size of the array (in bytes)
print("Item size of the array (in bytes):", arr.itemsize) # 4 bytes for int32, 8 bytes for int64, as each character is stored as 4 bytes in numpy (default for string data type), so 21 characters * 4 bytes = 84 bytes

# total size of the array (in bytes)
print("Total size of the array (in bytes):", arr.nbytes) # itemsize * size = 84 bytes * 9 elements = 756 bytes
