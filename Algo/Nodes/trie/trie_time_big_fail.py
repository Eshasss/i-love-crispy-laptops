# Это была попытка сделать эпичные полностью автоматические тесты, но тут надо мучаться с юникодом и все сломалось...


from tree import Dict
from Algo.Nodes.trie.trie import Trie 
import timeit

import random

def str_maker(length, start, end):
    start_int = int(start, 16)
    end_int = int(end, 16)
    random_string = ''.join(chr(random.randint(start_int, end_int)) for _ in range(length))
    return random_string

def strs_maker(amount: int, length: str, start="0x00AB", end="0x10FFFF"):
    """
    Делает данные 
    """
    strs = []
    for i in range(amount):
        strs.append(str_maker(length, start, end))
    return strs



def add_trie(data):
    t = Trie()
    print('pi')
    for i in range(len(data)):
        try:
            t.add(data[i])
        except:
            print(data[i])



# def add_set():

# def cont_trie():

# def cont_set():

# def del_trie():

# def del_set():
# 1.1 Строки из 10 символов. 
d1 = strs_maker(10, 20)
# 1.2. Строки из 100 символов.
d2 = strs_maker(100, 20)
# 1.3. Строки из 1000 символов
d3 = strs_maker(1000, 20)
# 1.4. Строки из 10000 символов.
d4 = strs_maker(10000, 20)
print(d1)
timer_(add_trie(d1))
# 2.1 Строки из первых 500 юникод символов (10)
# 2.2 Строки из первых 500 юникод символов (100)
# 2.3 Строки из первых 500 юникод символов (1000)
# 2.4 Строки из первых 500 юникод символов (10000)

# 3.1 Строки из последних 500 юникод символов (10)
# 3.2 Строки из последних 500 юникод символов (100)
# 3.3 Строки из последних 500 юникод символов (1000)
# 3.4 Строки из последних 500 юникод символов (10000)