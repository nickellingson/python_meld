import numpy as np

# Understand dimensions (visualize)
test_arr = np.array([1,2,3,4,5,6])
print("Array\n", test_arr)
print("Shape", test_arr.shape)
print("Dtype", test_arr.dtype)
print("Ndim", test_arr.ndim)
# Reshape, 
# Reshape, add dimension, (can add as many 1 dimensions as we want)
print("Reshape")
print(test_arr.reshape(6,1))
print()

test_arr2 = np.array([
                      [1,2,3], 
                      [4,5,6]
                    ]) # or [[1,2,3,4,5,6]] (2d)
print("Array\n", test_arr2)
print("Shape", test_arr2.shape)
print("Dtype", test_arr2.dtype)
print("Ndim", test_arr2.ndim)
# Reshape vs. transpose
# Reshape keeps numbers in order
print("Reshape")
print(test_arr2.reshape(3, 2))
print("Transpose")
print(test_arr2.T)
print()

test_arr3 = np.array([
                        [
                            [1,2],
                            [3,4],
                            [5,6]
                        ]
                    ]) # or [[[1,2,3,4,5,6]]] (3d)
print("Array\n", test_arr3)
print("Shape", test_arr3.shape)
print("Dtype", test_arr3.dtype)
print("Ndim", test_arr3.ndim)
print()

# Slicing
# 2d
# arr[row, column, step]

# 3d
# arr[block (depth), row within block, column within row]