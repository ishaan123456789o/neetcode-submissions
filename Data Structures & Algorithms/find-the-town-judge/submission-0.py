class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        howManyPeopleTrust = defaultdict(int)
        trustsSomeone = set()
        for pair in trust:
            howManyPeopleTrust[pair[1]] += 1
            trustsSomeone.add(pair[0])
        target = n-1
        for key in howManyPeopleTrust.keys():
            if howManyPeopleTrust[key] == target and key not in trustsSomeone:
                return key
        return -1

        