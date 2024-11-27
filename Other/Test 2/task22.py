def lg(x): # находит кол-во необходимых действий  
    n = 0 
    while x != 0: 
        x = x // 3 
        n += 1 
    return n 
 
def solver(l, r): 
    k1 = lg(l) 
    answer = k1 * 2 
    l += 1 
    print(answer)
    while 3 ** k1 <= r: 
        answer += (3 ** (k1) - l) * k1 
        l = 3 ** (k1) 
        k1 += 1 
    print(answer) 
    answer += k1 * (r - l + 1) 
    return answer 
 
 
# 2000000 
def pre_processor(l, r): 
    answer = 0 
    logs3 = [3 ** i for i in range(14)] 
    k = lg(l) 
    answer += k * 2 
    print(answer) 
    for i in range(k+1, 14): 
        if logs3[i] > r: 
            break
        else: 
            answer += (logs3[i] - logs3[i-1])*(i+1) 

    print(answer) 
    print('()',  (r - logs3[i-1] + 1) * (i)) 
    answer += (r - logs3[i-1] + 1) * (i) 
     
    return answer 
     
print(pre_processor(19, 84)) 
print('-------') 
print(solver(19, 84)) 
 
 
    #     if logs3[i] >= r: 
    #         break 
 
    #     if f: 
    #         answer += (logs3[i] - logs3[i-1]) * (i + 1) 
 
    #     if logs3[i] >= l: 
    #         answer += (i) * 2 
    #         f = True 
    # print('add-on:',(r - logs3[i-1]) * i) 
    # answer += (r - logs3[i-1]) * (i) 
 
    #return answer 
     
# print(pre_processor(0,3)) 
# print(pre_processor(1,3)) 
# print(pre_processor(2, 4)) 
# print(pre_processor(1999999, 2000000)) 


# print(solver(1, 3))   
# print(solver(2, 4))  
# print(solver(1999999, 2000000)) 

# print(solver(0,4)) 
 
 
# n = int(input()) 
# for i in range(n): 
#     l, r = map(int, input().split()) 
#     print(solver(l, r)) 
 
 
 
 
 
# def solver2(l, r): 
#     k1 = lg(l) 
#     k2 = lg(r) 
#     answer = k1 * 2 
#     l += 1 
#     for i in range(k1, k2): 
#         answer += (3**(i) - l) * i 
#         l = 3**(i)  
#     answer += k2*(r-l+1) 
#     return answer 
 
 
# def solver3(l, r): 
#     k1 = lg(l) 
#     k2 = lg(r) 
#     answer = k1 * 2 
#     l += 1 
#     for i in range(k1, k2 + 1): 
#         while l <= r and l <= 3 ** i: 
#             answer += i 
#             l += 1   
#     return answer + k2 - k1n