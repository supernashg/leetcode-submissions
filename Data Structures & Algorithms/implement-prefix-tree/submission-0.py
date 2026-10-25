class PrefixTree:

    def __init__(self):
        self.data = defaultdict(set)
        
    def insert(self, word: str) -> None:
        char = word[0]
        self.data[char].add(word)

    def search(self, word: str) -> bool:
        char = word[0]
        return word in self.data[char]

    def startsWith(self, prefix: str) -> bool:
        char = prefix[0]
        for word in self.data[char]:
            if word.startswith(prefix): return True
        return False

