import copy
import numpy as np


# 1.1
def sum_non_neg_diag(X: list, ans = 0) -> int:
    i = len(X)
    j = len(X[0])
    if i > j:
        i, j = j, i
    for i in range(len(X[0])):
            if X[i][i] >=0:
                ans += X[i][i]
    return ans


# 2.1
def mul2(x: list, y: list) -> bool:
    z = copy.deepcopy(x)
    if len(x) != len(y):
        return False
    for i in z:
        if i in y:
            x.remove(i)
            y.remove(i)
        else:
            return False
    return True

def are_multisets_equal(x: list, y: list) -> bool:
    return sorted(x) == sorted(y)


# 3.1
def max_prod_mod_3(x: list, rec = float('-inf')) -> int:
    for i in range(0, len(x)-1):
        if x[i+1] % 3 == 0 or x[i] % 3 == 0:
            rec = max(x[i]*x[i+1], rec)
    if rec == float('-inf'):
        return -1
    return rec


#4.1 
def convert_image(image: list, weights: list) -> list:
    y = len(image)
    x = len(image[0])
    z = len(weights)
    ans = [[0 for i in range(x)] for j in range(y)]
    for i in range(y):
        for j in range(x):
            for channel in range(z):
                ans[i][j] += image[i][j][channel] * weights[channel]
    return ans


# 5.1
def rle_scalar(x: list, y: list):
    x1 = []
    y1 = []
    answer = 0
    for i in x:
        x1.extend([i[0]]*i[1])
    for i in y:
        y1.extend([i[0]]*i[1])
    if len(x1) != len(y1):
        return -1
    for i in range(len(x1)):
        answer += x1[i]*y1[i]
    return answer
    