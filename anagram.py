from dictionary import Dictionary

class Anagram(object):
    
    def __init__(self):
        self.possible_words = set()
        self.output = set()
        self.dict = Dictionary()
        fich = open('Unabr.dict', 'r')
        self.dict.get_dict(fich)
        fich.close()
        
    def set_input(self, string):
        self.string = string
        
    def get_output(self):
        self.process('', list(self.string))
        for word in self.possible_words:
            if self.dict.is_in_dict(word):
                self.output.add(word)
        return self.output
    
    def process(self, string, l):
        if len(l) == 0:
            self.possible_words.add(string)
            return
        for index in range(len(l)):
            new_list = l[:]
            elem = new_list.pop(index)
            self.process(string + elem, new_list)            