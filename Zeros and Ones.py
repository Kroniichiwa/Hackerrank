import numpy as np
dim = tuple(map(int, input().strip().split(' ')))
print(np.zeros(dim, dtype = np.int32), np.ones(dim, dtype = np.int32), sep = '\n')