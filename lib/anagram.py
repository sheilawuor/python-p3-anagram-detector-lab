class Anagram:
    def __init__(self, word):
        self.word = word.lower()
    
    def match(self, possible_anagrams):
        matches = []
        word_sorted = sorted(self.word)
        
        for candidate in possible_anagrams:
            if sorted(candidate.lower()) == word_sorted:
                matches.append(candidate)
        
        return matches
