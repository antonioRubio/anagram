import unittest
from anagram import Anagram

class TestAnagram(unittest.TestCase):
    def setUp(self):
        self.anagram = Anagram()
        
    def test_one_letter(self):
        self.anagram.set_input("a")
        output = self.anagram.get_output()
        self.assertEquals(set([]), output)
    
    def test_two_letters(self):
        self.anagram.set_input("ac")
        output = self.anagram.get_output()
        self.assertEquals(set([]), output)
        
    def test_two_equal_letters(self):
        self.anagram.set_input("aa")
        output = self.anagram.get_output()
        self.assertEquals(set(["aa"]), output)
        
    def test_three_equal_and_four_letters(self):
        self.anagram.set_input("sses")
        output = self.anagram.get_output()
        self.assertEquals(set(["sess"]), output)
        
    def test_three_different_letters(self): 
        self.anagram.set_input("abc")
        output = self.anagram.get_output()
        self.assertEquals(set(["bac"]), output)
        
if __name__ == '__main__':
    unittest.main()
