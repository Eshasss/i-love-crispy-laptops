cps = [100, 20, 10, 5, 1]
count = 0
n = int(input())
for c in cps:
    #print(c, n, count, n//c)
    if c <= n:
        count += n//c
        n-=(n//c)*c
        #print(c, n, count, n//c)
        
print(count)
