def lg(x):
    n = 0
    while x!=0:
        x = int(x/3)
        n+=1
    return n
    
    
def solver(l, r):
    answer =0
    k = lg(l)
    answer += 2*k
    l += 1
    answer += (3**(k+1) -l)*(k+1)
    l=3**(k+1)
    #k+=1
   
    while 3**(k+1) < r:
        answer +=(3**(k+1) -l)*(k+1)
        k+=1
        l=3**(k+1)
    answer += (r - 3**k) * (k+1)
    return answer
        
print(solver(1, 3))
print(solver(2, 4))
print(solver(1999999, 2000000))
print(solver(19, 84))