def lg(x): # находит кол-во необходимых действий 
    n = 0
    while x != 0:
        x = int(x/3)
        n += 1
    return n

def solver2(l, r):
    k1 = lg(l)
    k2 = lg(r)
    answer = k1 * 2
    l += 1
    for i in range(k1, k2):
        answer += (3**(i) - l) * i
        l = 3**(i) 
    answer += k2*(r-l+1)
    return answer


def solver3(l, r):
    k1 = lg(l)
    k2 = lg(r)
    answer = k1 * 2
    l += 1
    for i in range(k1, k2 + 1):
        while l <= r and l <= 3 ** i:
            answer += i
            l += 1  
    return answer + k2 - k1

def solver(l, r):
    k1 = lg(l)
    answer = k1 * 2
    l += 1
    while 3 ** k1 <= r:
        answer += (3 ** (k1) - l) * k1
        l = 3 ** (k1)
        k1 += 1
    answer += k1 * (r - l + 1)
    return answer

print(solver(1, 3), solver2(1, 3))  
print(solver(2, 4), solver2(2, 4)) 
print(solver(1999999, 2000000), solver2(1999999, 2000000))
print(solver(19, 84), solver2(19, 84))
print(solver(0,4))
