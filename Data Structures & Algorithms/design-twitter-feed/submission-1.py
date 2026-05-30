import itertools
class Twitter:

    def __init__(self):
        self.following = defaultdict(set)
        self.followers = defaultdict(set)
        self.feed = []
        self.counter = itertools.count()
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        heapq.heappush(self.feed, (-next(self.counter), (userId, tweetId)))

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        reapply = []
        while len(res) < 10 and self.feed:
            curr = heapq.heappop(self.feed)
            reapply.append(curr)
            if curr[1][0] == userId or curr[1][0] in self.following[userId]:
                res.append(curr[1][1])
        for entry in reapply:
            heapq.heappush(self.feed, entry)
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)
        self.followers[followeeId].add(followerId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
            self.followers[followeeId].remove(followerId)
