class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        numGroups = len(hand) // groupSize
        hand.sort()
        finishedGroups = 0
        startedGroups = 0
        lastElementToLength = defaultdict(list)
        for num in hand:
            if num-1 in lastElementToLength:
                curr = lastElementToLength[num-1].pop()
                if curr + 1 == groupSize:
                    finishedGroups += 1
                    startedGroups -= 1
                else:
                    lastElementToLength[num].append(curr+1)
                if len(lastElementToLength[num-1]) == 0:
                        del lastElementToLength[num-1]
            elif startedGroups + finishedGroups == numGroups:
                return False
            else:
                if groupSize == 1:
                    finishedGroups += 1
                else:
                    lastElementToLength[num].append(1)
                    startedGroups += 1
        if finishedGroups == numGroups:
            return True
        return False


        