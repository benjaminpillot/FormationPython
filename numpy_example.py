# -*- coding: utf-8 -*-

""" Module summary description.

More detailed description.
"""

import numpy as np


random_array_0_1 = np.random.randint(0, high=2, size=(5, 5))
random_array_0_9 = np.random.randint(0, high=10, size=(5, 5))
new_array = random_array_0_9.copy()
new_array2 = random_array_0_9.copy()
new_array[random_array_0_1 == 0] = random_array_0_9[random_array_0_1 == 0] * 3
new_array2[(random_array_0_9 > 2) & (random_array_0_9 < 8)] = random_array_0_1[(random_array_0_9 > 2) & (
        random_array_0_9 < 8)]

new_array[np.isnan(random_array_0_1)] = random_array_0_1[np.isnan(random_array_0_1)]

print("Number of dimensions of array: %d" % random_array_0_9.ndim)
print("Shape of array: {}".format(random_array_0_9.shape))
print("Size of array (number of elements): %d" % random_array_0_9.size)
print("Max value of array: %d" % random_array_0_9.max())
print("Average of values in array: %.3f" % random_array_0_9.mean())

print(random_array_0_1)
print(random_array_0_9)
print(new_array)
print(new_array2)
