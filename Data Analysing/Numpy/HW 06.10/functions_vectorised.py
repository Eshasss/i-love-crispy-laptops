import numpy as np


# 1.2
X = np.array([[-1, 0, 1], [2, 0, 2], [3, 0, 3], [4, 4, 4]])
def sum_non_neg_diag_vec(X: list) -> int:
    return np.diagonal(X)[np.diagonal(X)>0].sum()


# 2.2
def are_multisets_equal_vec(x: np.array, y: np.array) -> bool:
    return (np.sort(x) == np.sort(y)).all()


# 3.2
def max_prod_mod_3_vec(x: np.array) -> int:
    muls = x[:-1] * x[1:]
    return np.max(muls[(x[:-1] % 3 == 0) | (x[1:] % 3 == 0)], initial=-1)


#4.2 
def convert_image_vec(image: np.array, weights: np.array) -> np.array:
    return np.tensordot(image, weights, axes=([2], [0]))


# 5.2
x = np.array([[1, 2], [2, 3], [3, 1]])
y = np.array([[1, 1], [0, 5]])

def rle_scalar_vec(x: np.array, y:np.array):
    x1 = np.repeat(x[:, 0], x[:, 1])
    y1 = np.repeat(y[:, 0], y[:, 1])
    if x1.shape != y1.shape:
        return -1
    return np.dot(x1, y1)
