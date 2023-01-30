import numpy as np

def key_to_matrix(key: str):
    size = int(len(key) ** 0.5)
    kmatrix = np.zeros((size, size))
    kmatrix = np.array([[ord(c) - ord('a') for c in key[i:i+size]] for i in range(0, len(key), size)])
    return kmatrix

key = "gybnelite"
kmatrix = key_to_matrix(key)
print(kmatrix)