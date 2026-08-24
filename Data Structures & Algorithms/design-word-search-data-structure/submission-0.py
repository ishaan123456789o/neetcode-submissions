class TrieNode:
    def __init__(self):
        self.children = {}
        self.value = ""

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch in curr.children:
                curr = curr.children[ch]
            else:
                new = TrieNode()
                new.value = ch
                curr.children[ch] = new
                curr = new
        if '/' not in curr.children:
            curr.children['/'] = TrieNode()

    def search(self, word: str) -> bool:
        q = deque()
        q.append(self.root)
        index = 0
        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                if index == len(word):
                    if '/' in curr.children:
                        return True
                else:
                    if word[index] in curr.children:
                        q.append(curr.children[word[index]])
                    elif word[index] == '.':
                        for key in curr.children.keys():
                            q.append(curr.children[key])
            index += 1
        return False

        
