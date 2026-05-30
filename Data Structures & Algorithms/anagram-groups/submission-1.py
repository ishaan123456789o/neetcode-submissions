class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counterMap = {}
        lisMap = defaultdict(list)
        num = 1
        counterMap[1] = Counter(strs[0])
        lisMap[1].append(strs[0])
        for i in range(1, len(strs)):
            word = strs[i]
            curr = Counter(word)
            matched = None
            for key in counterMap.keys():
                matched = True
                compare = counterMap[key]
                if len(compare) != len(curr):
                    matched = False
                else:
                    for k in compare.keys():
                        if k not in curr or compare[k] != curr[k]:
                            matched = False
                            break
                if matched:
                    lisMap[key].append(word)
                    break
            if matched == False:
                num += 1
                counterMap[num] = curr
                lisMap[num].append(word)
        return list(lisMap.values())

            
        