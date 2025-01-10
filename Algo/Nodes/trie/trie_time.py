from tree import Set
from Algo.Nodes.trie.trie import Trie 
import timeit


def get_d(data):
    e = []
    for i in data:
        e.extend(list(i))
    s =  list(set(e))
    d = {"\0": {}}
    for i in s:
        d[i] = {}
    return d

def add_trie(data, d):
    t = Trie(d)
    for i in range(len(data)):
        t.add(data[i])
    return t

def add_set(data):
    s = Set([data[0]])
    for i in range(1, len(data)):
        s.add(data[i])
    return s

def cont_trie(data, t:Trie):
    for i in range(0, len(data)):
        t.contains(data[i])

def cont_set(data, s:Trie):
    for i in range(0, len(data)):
        s.__contains__(data[i])
        

d1 = ["a"*10,
      "b"*10,
      "c"*10,
      "d"*10,
      "e"*10,
      "f"*10,
      "g"*10,
      "h"*10]
d1d = get_d(d1)

d2 = ["abcd", "bbcd", "cbcd", "dbcd",
      "aacd", "accd", "adcd",
      "abad", "abdd",
      "abca"]
d2d = get_d(d2)

d3 = ["abcdrf",
      "автобус",
      "tururur",
      "idkwhat",
      "ёшкиауф",
      "вээвээв",
      "хэппиньюэ"
]
d3d = get_d(d3)

d1ad = add_trie(d1, d1d)
d2ad = add_trie(d2, d2d)
d3ad = add_trie(d3, d3d)

s1ad = add_set(d1)
s2ad = add_set(d2)
s3ad = add_set(d3)


add_t1 = timeit.timeit(lambda: add_trie(d1, d1d), number=10000)
add_s1 = timeit.timeit(lambda: add_set(d1), number=10000)

add_t2 = timeit.timeit(lambda: add_trie(d2, d2d), number=10000)
add_s2 = timeit.timeit(lambda: add_set(d2), number=10000)

add_t3 = timeit.timeit(lambda: add_trie(d3, d3d), number=10000)
add_s3 = timeit.timeit(lambda: add_set(d3), number=10000)

cont_t1 = timeit.timeit(lambda: cont_trie(d1, d1ad), number=10000)
cont_s1 = timeit.timeit(lambda: cont_set(d1, s1ad), number=10000)

cont_t2 = timeit.timeit(lambda: cont_trie(d2, d2ad), number=10000)
cont_s2 = timeit.timeit(lambda: cont_set(d2, s2ad), number=10000)

cont_t3 = timeit.timeit(lambda: cont_trie(d3, d3ad), number=10000)
cont_s3 = timeit.timeit(lambda: cont_set(d3, s3ad), number=10000)

print(f"Добавление: повтороки: trie: {add_t1} set: {add_s1}")
print(f"Добавление: одинаковые префиксы: trie: {add_t2} set: {add_s2}")
print(f"Добавление: разные префиксы: trie: {add_t3} set: {add_s3}")
print("--------")
print(f"Поиск: повторок: trie: {cont_t1} set: {cont_s1}")
print(f"Поиск: одинаковые префиксы: trie: {cont_t2} set: {cont_s2}")
print(f"Поиск: разные префиксы: trie: {cont_t3} set: {cont_s3}")

# Ура! Префиксное дерево действительно быстрее работает. 
# Кстати говоря, когда разные префиксы разница особо ощутима. 
# Когда добавляются элементы с многим повтором (типа "аааааа") БОР проигрывает, 
# ну скорее потому что он не сжатый