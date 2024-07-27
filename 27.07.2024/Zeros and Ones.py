import numpy as np

shape = tuple(map(int, input().strip().split()))

zeros_array = np.zeros(shape, dtype=int)

ones_array = np.ones(shape, dtype=int)

print(zeros_array)
print(ones_array)
