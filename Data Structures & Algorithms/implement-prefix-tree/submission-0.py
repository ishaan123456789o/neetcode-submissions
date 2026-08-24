class TrieNode:
    def __init__(self):
        self.childByCharacter = {}
        self.value = ''
class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch in curr.childByCharacter:
                curr = curr.childByCharacter[ch]
            else:
                new = TrieNode()
                new.value = ch
                curr.childByCharacter[ch] = new
                curr = new
        if '/' not in curr.childByCharacter:
            curr.childByCharacter['/'] = TrieNode()

    def search(self, word: str) -> bool:
        curr = self.root
        for ch in word:
            if ch not in curr.childByCharacter:
                return False
            curr = curr.childByCharacter[ch]
        if '/' not in curr.childByCharacter:
            return False
        return True
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for ch in prefix:
            if ch not in curr.childByCharacter:
                return False
            curr = curr.childByCharacter[ch]
        return True
        