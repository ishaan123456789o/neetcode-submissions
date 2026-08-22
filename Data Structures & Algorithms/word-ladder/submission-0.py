class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        words = set(wordList)
        if endWord not in words:
            return 0
        adjList = defaultdict(list)
        if beginWord not in words:
            wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                for letter in letters:
                    curr = word[:i] + letter + word[i+1:]
                    if curr in words:
                        adjList[word].append(curr)
        q = deque()
        q.append(beginWord)
        seen = set()
        res = 1
        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                if curr == endWord:
                    return res
                seen.add(curr)
                for neighbor in adjList[curr]:
                    if neighbor not in seen:
                        q.append(neighbor)
            res += 1
        return 0
        