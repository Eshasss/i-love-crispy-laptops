from __future__ import annotations


class TrieNode:
    nodes: dict[str, TrieNode]

    def __init__(self, d) -> None:
        """
        Есть небольшой прикол с инициализацией здесь. 
        Если символ никогда не будет использован, то он будет иметь значение словаря.
        А если хоть раз был использован(но мб позже удален), то он будет узлом.
        Плаки-плаки.
        Если не дан словарь пользователем, то будут все символы юникода.
        """
        if d is not None and isinstance(d, dict):

            self.start = d
            self.nodes = d
        else:
            # Эта штука плохо работает лучше не трогать
            self.start = {chr(code): {} for code in range(0x110000) if chr(code).isprintable()}
            self.nodes = {chr(code): {} for code in range(0x110000) if chr(code).isprintable()}



    def __repr__(self) -> str:
        return self.nodes.__str__()
    
    def add(self, s:str):
        if s == "":
            self.nodes["\x00"] = TrieNode(self.start)
            return 
        if self.nodes[s[0]] == {}: 
            self.nodes[s[0]] = TrieNode(self.start)
        self.nodes[s[0]].add(s[1::])

    def delete(self, s: str):
        if s == "":
            self.nodes["\x00"] = {}
            return 
        l = s[0]
        self.nodes[l].delete(s[1::])
    
        
class Trie:
    root: TrieNode

    def __init__(self, d=None) -> None:
        self.root = TrieNode(d)
        self.words = []
    
    def add(self, s:str):
        if s not in self.words:
            self.words.append(s)
            self.root.add(s)

    def get_all_words(self):
        return self.words

    def contains(self, s: str) -> bool:
        if s in self.words:
            return True
        return False

    def delete(self, s: str) -> None:
        if self.contains(s):
            self.words.remove(s)
            self.root.delete(s)
        else:
            raise ValueError(f"Value {s} is not in the dict.")
    
    # def w(self):
    #     return self.root.w()
        


# tr = Trie({"a":{}, "b":{}, "c":{}, "\0":{}})
# # print(tr.root)
# tr.add("a")
# tr.add("ac")
# tr.add("abc")
# tr.add("c")

# #print('Тип моего супермегакрутого дерева', type(tr))
# print("-----------")

# print(tr.words)
# tr.delete("abc")
# print(tr.words)
# tr.add("abc")
# print(tr.words)
# print(tr.root.nodes)
    # def w(self, ans=[], curr=''):
    #     print(self.nodes)
    #     print("-----------")

    #     for k, v in self.nodes.items():
    #         if v != {}:
    #             self.nodes[k].w(ans, curr=curr+k)
    #             if self.nodes['\x00'] != {} and self.nodes['\x00'] not in ans:
    #                 print('appendus')
    #                 ans.append(curr)

    #     return ans


    # """
    # 1) Реализовать класс узла префиксного дерева и класс префиксного дерева. Дерево должно хранить множество строк способом, указанным на лекции в классе.
    # 2) Протестировать полученные классы с помощью pytest/unittest
    # 3) Найти примеры на которых set[str] показывает себя эффективнее и примеры для которы эффективнее будет полученное дерево
    # 4) * Вместо стандартного класса dict использовать написанный ранее класс AVLDict/Dict
    # 5) * Реализовать сжатое префиксное дерево, то есть такое, которое в одном узле хранит символы не по одному, а строками по несколько
    # """