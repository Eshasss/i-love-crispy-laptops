logs3 = [1, 3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049, 177147, 531441, 1594323, 14348907]

def lg(x): # находит кол-во необходимых действий  
    n = 0 
    while x != 0: 
        x = x // 3 
        n += 1 
    return n 

def solver(l, r): # работает за (log3(r) - log3(l)) + log3(l) = log3(r) действий Худший случай - 14
    k = lg(l)
    answer = k * 2 
    l += 1

    for i in range(k, 15):
        if logs3[i] > r:
            answer += (r - l + 1) * (i)
            break
        answer += (logs3[i] - l) * i
        l = logs3[i]

    return answer

n = int(input())
for i in range(n):
    l, r = map(int, input().split())
    print(solver(l, r))


# print(solver(1,3))
# print(solver(2,4))
# print(solver(1999999,2000000))
# print(solver(19,84))