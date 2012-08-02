class Dictionary(object):
    def __init__(self):
        self.words = set()
        
    def get_dict(self, f):
        for line in f:
            word = line[:-1]
            self.words.add(word)
            
    def is_in_dict(self, word):
        return word in self.words