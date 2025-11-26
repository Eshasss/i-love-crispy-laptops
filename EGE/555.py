
def f(n):
    b_n = bin(n)
    print(b_n)
    # print("cut", b_n[2:])
    b_n_cut = b_n[2:]
    new_b = ""
    for i in range(len(b_n_cut)-1, -1, -1):
        new_b += b_n_cut[i]

    while new_b[0] == "0":
        # print(new_b)

        new_b = new_b[1::]

    return int(new_b,2)
maxx = 0
for i in range(1,100):
    if f(i) == 11:
        maxx = i

print(maxx)
# print("bez", new_b)
# print(int(new_b,2))
# print(b_n_cut[:i])