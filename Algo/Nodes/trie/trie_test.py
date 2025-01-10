import unittest
from Algo.Nodes.trie.trie import Trie 

class TestTrie(unittest.TestCase):

    def setUp(self):
        self.trie = Trie({"a":{}, "b":{}, "c":{}, "d":{}, "e":{}, "f":{}, "g":{}, "h":{}, "i":{}})
        
    def test_add_single_word(self):
        self.trie.add("abc")
        self.assertIn("abc", self.trie.get_all_words())
    
    def test_add(self):
        """Тестируем добавление нескольких слов"""
        self.trie.add("abc")
        self.trie.add("def")
        self.trie.add("ghi")
        self.assertIn("abc", self.trie.get_all_words())
        self.assertIn("def", self.trie.get_all_words())
        self.assertIn("ghi", self.trie.get_all_words())
    
    def test_delete(self):
        self.trie.add("abc")
        self.trie.delete("abc")
        self.assertNotIn("abc", self.trie.get_all_words())
    
    def test_delete_non_existent_word(self): # Ловим ошибку
        with self.assertRaises(ValueError):
            self.trie.delete("хохо")
    
    def test_contains(self):
        self.trie.add("abc")
        self.assertTrue(self.trie.contains("abc"))
        self.assertFalse(self.trie.contains("хохохо"))
    
    def test_tudasuda(self):

        self.trie.add("abc")
        self.trie.add("abcde")
        self.trie.add("bcde")
        self.trie.add("bcdeee")
        self.assertIn("abc", self.trie.get_all_words())
        self.assertIn("abcde", self.trie.get_all_words())
        self.assertIn("bcde", self.trie.get_all_words())
        self.assertIn("bcdeee", self.trie.get_all_words())
        self.trie.delete("abc")
        self.assertNotIn("abc", self.trie.get_all_words())
        self.assertIn("abcde", self.trie.get_all_words()) # "предок" остался урааа

if __name__ == "__main__":
    unittest.main()