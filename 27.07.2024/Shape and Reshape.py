import numpy

input_list = list(map(int, input().strip().split()))
array_3x3 = np.array(input_list).reshape(3, 3)

print(array_3x3)
