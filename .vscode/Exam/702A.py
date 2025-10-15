n = int(input())
a = input().split(" ")
maxcur = 0
for i in range(n):
    cur = 0
    r = a[i]
    chance = True
    for j in range(n):
        # print("сейчас некст")
        # print(j, a[j], a[j] >= r, r)
        if a[j] == a[i] and chance:
            chance = False
            cur += 1
            r = a[i]

        elif a[j] > r:
            cur += 1
            r = a[j]
            # print("нижгрань", r, a[j], j)
    # print(j,r )
    if cur > maxcur:
        maxcur = cur

print(maxcur)
