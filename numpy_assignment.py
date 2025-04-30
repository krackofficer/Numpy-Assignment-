
# NumPy Assignment - Questions and Answers

"""
1. Explain the purpose and advantages of NumPy in scientific computing and data analysis. How does it enhance Python's capabilities for numerical operations?
"""
# Answer:
# NumPy provides support for large, multi-dimensional arrays and matrices, along with a collection
# of mathematical functions to operate on them. It enhances Python by offering faster computations,
# vectorization, broadcasting, and efficient memory usage.

"""
2. Compare and contrast np.mean() and np.average() functions in NumPy. When would you use one over the other?
"""
# Answer:
# np.mean() calculates the simple arithmetic mean.
# np.average() allows weights to be assigned to elements for a weighted mean.
# Use np.mean() for regular average and np.average() for weighted averages.

"""
3. Describe the methods for reversing a NumPy array along different axes. Provide examples for 1D and 2D arrays.
"""
# Answer:
import numpy as np
arr1d = np.array([1, 2, 3, 4])
reversed_1d = arr1d[::-1]

arr2d = np.array([[1,2,3],[4,5,6]])
reversed_rows = arr2d[::-1, :]
reversed_columns = arr2d[:, ::-1]

"""
4. How can you determine the data type of elements in a NumPy array? Discuss the importance of data types in memory management and performance.
"""
# Answer:
# Use array.dtype to determine the data type.
# Correct data types optimize memory usage and performance by allocating minimal required space.

"""
5. Define ndarrays in NumPy and explain their key features. How do they differ from standard Python lists?
"""
# Answer:
# ndarrays are homogeneous, multi-dimensional arrays supporting element-wise operations, broadcasting,
# and memory efficiency. They differ from lists by being faster and supporting mathematical operations directly.

"""
6. Analyze the performance benefits of NumPy arrays over Python lists for large-scale numerical operations.
"""
# Answer:
# NumPy arrays are faster due to contiguous memory storage, C-based implementation, and support for
# vectorized operations, avoiding slow Python loops.

"""
7. Compare vstack() and hstack() functions in NumPy. Provide examples demonstrating their usage and output.
"""
# Answer:
a = np.array([1,2,3])
b = np.array([4,5,6])

vertical_stack = np.vstack((a,b))
horizontal_stack = np.hstack((a,b))

"""
8. Explain the differences between fliplr() and flipud() methods in NumPy, including their effects on various array dimensions.
"""
# Answer:
# fliplr() flips the array left to right (columns reversed).
# flipud() flips the array upside down (rows reversed).

"""
9. Discuss the functionality of the array_split() method in NumPy. How does it handle uneven splits?
"""
# Answer:
arr = np.arange(10)
split_arr = np.array_split(arr, 3)
# array_split() divides arrays into nearly equal parts, allowing uneven splits.

"""
10. Explain the concepts of vectorization and broadcasting in NumPy. How do they contribute to efficient array operations?
"""
# Answer:
# Vectorization applies operations to entire arrays without loops.
# Broadcasting automatically expands array dimensions to allow operations between differently shaped arrays.
# Both improve speed and simplify code.
