# bin(n) 2-ричная
# oct(n) 8-ричная
# hex(n) 16-ричная
# format(n, "b")

# int(bin_n, X) X - система
# zfill(n, 8)

def f(n):
    ostatok = n%4
    bin_n = str(format(n, 'b')) + str(format(ostatok, 'b'))
    return int(bin_n,2)
r = [0]*1000
for i in range(66):
    r[(f(i))] = 1


print(sum(r[0:65]))
print(len(r))