'''Тестировка верности решений '''

from functions import sum_non_neg_diag, are_multisets_equal, max_prod_mod_3, rle_scalar, convert_image
from functions_vectorised import sum_non_neg_diag_vec, are_multisets_equal_vec, max_prod_mod_3_vec, rle_scalar_vec, convert_image_vec

import numpy as np

sum_non_neg_diag_data = []
for n in [10, 100, 1000, 10000]:
    X = np.random.randint(0, 3, (n, n))
    sum_non_neg_diag_data += [X]

are_multisets_equal_data = []
for n in [10, 100, 1000, 10000]:
    x = np.random.randint(0, 2, n)
    y = np.random.randint(0, 2, n)
    are_multisets_equal_data += [(x, y)]

max_prod_mod_3_data = []
for n in [10, 100, 1000, 10000]:
    x = np.random.randint(1, 100, n)
    max_prod_mod_3_data += [x]

convert_image_data = []
for n in [10, 100, 1000]:
    image = np.random.random((n, n, 10))
    weights = np.random.random(10)
    convert_image_data += [(image, weights)]

rle_scalar_data = []
for n in [10, 100, 1000, 10000]:
    x = np.random.randint(1, 3, (n, 2))
    y = np.random.randint(1, 3, (n, 2))
    shapes = np.random.randint(1, 3, n)
    x[:, 1] = shapes
    y[:, 1] = shapes

    rle_scalar_data += [(x, y)]

cosine_distance_data = []
for n in [10, 100]:
    X = np.random.random((n, n))
    Y = np.random.random((n, n))
    cosine_distance_data += [(X, Y)]

def test_sum_non_neg_diag():
    for p in sum_non_neg_diag_data:
        assert sum_non_neg_diag_vec(p) == sum_non_neg_diag(p)

def test_are_multisets_equal():
    for p in are_multisets_equal_data:
        assert are_multisets_equal_vec(p[0], p[1]) == are_multisets_equal(p[0], p[1])

def test_max_prod_mod_3():
    for p in max_prod_mod_3_data:
        assert max_prod_mod_3_vec(p) == max_prod_mod_3(p)

def test_rle_scalar():
    for p in rle_scalar_data:
        assert rle_scalar_vec(p[0], p[1]) == rle_scalar(p[0], p[1])

def test_convert_image():
    for p in convert_image_data:
        #Тест верный,  но не очень (см. тетрадку)
        assert np.array_equal(convert_image_vec(p[0], p[1]), convert_image(p[0], p[1]))