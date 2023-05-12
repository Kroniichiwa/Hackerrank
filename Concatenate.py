import numpy as np

N, M, P = map(int, input().split())

array_N = []
for _ in range(N):
    row = list(map(int, input().split()))
    array_N.append(row)

array_M = []
for _ in range(M):
    row = list(map(int, input().split()))
    array_M.append(row)

concatenated_array = np.concatenate((array_N, array_M), axis=0)
print(concatenated_array)
