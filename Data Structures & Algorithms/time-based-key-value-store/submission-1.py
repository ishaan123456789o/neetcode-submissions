class TimeMap:

    def __init__(self):
        self.keyToVal = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keyToVal[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        currentList = self.keyToVal[key]
        l = 0
        r = len(currentList)-1
        res = (-1, None)
        while l <= r:
            mid = l + (r-l)//2
            if timestamp == currentList[mid][0]:
                res = currentList[mid]
                break
            if currentList[mid][0] > timestamp:
                r = mid - 1
            else:
                if res[0] < currentList[mid][0]:
                    res = currentList[mid]
                l = mid + 1
        if res[1]:
            return res[1]
        return ""

