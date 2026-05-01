import numpy as np

arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("Array:\n", arr)

# reshape of an array
reshaped_arr = arr.reshape(1,9)  # reshape the array to 1 row and 9 columns
print("Reshaped Array (1,9):\n", reshaped_arr)
reshaped_arr_2 = arr.reshape(9,1)  # reshape the array to 9 rows and 1 column
print("Reshaped Array (9,1):\n", reshaped_arr_2)

# flatten the array to 1D array
flattened_arr = arr.flatten()  # flatten the array to 1D array
print("Flattened Array:\n", flattened_arr)

# transpose of an array
transposed_arr = arr.T  # transpose (@property method)
print("Transposed Array using .T:\n", transposed_arr)
transposed_arr_2 = arr.transpose()  # transpose() method
print("Transposed Array using transpose() method:\n", transposed_arr_2)

# ravel of an array
raveled_arr = arr.ravel()  # ravel the array to 1D array, it returns a flattened array but it is a view of the original array, so if we change the values in the raveled array, it will change the values in the original array
print("Raveled Array:\n", raveled_arr)
raveled_arr[0] = 10  # changing the first element of the raveled array to 10
print("Raveled Array after modification:\n", raveled_arr)
print("Original Array after modification in raveled array:\n", arr)  # the original array is also modified because the raveled array is a view of the original array

