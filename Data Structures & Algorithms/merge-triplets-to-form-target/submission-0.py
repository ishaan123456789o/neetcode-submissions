class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        firstElement = defaultdict(list)
        secondElement = defaultdict(list)
        thirdElement = defaultdict(list)
        for triplet in triplets:
            first = triplet[0]
            second = triplet[1]
            third = triplet[2]
            firstElement[first].append(triplet)
            secondElement[second].append(triplet)
            thirdElement[third].append(triplet)
        for i in range(3):
            possible = False
            if i == 0:
                for triplet in firstElement[target[0]]:
                    if triplet[1] <= target[1] and triplet[2] <= target[2]:
                        possible = True
                        break
            elif i == 1:
                for triplet in secondElement[target[1]]:
                    if triplet[0] <= target[0] and triplet[2] <= target[2]:
                        possible = True
                        break
            else:
                for triplet in thirdElement[target[2]]:
                    if triplet[1] <= target[1] and triplet[0] <= target[0]:
                        possible = True
                        break
            if not possible:
                return False
        return True


        