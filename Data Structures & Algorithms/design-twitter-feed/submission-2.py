class Twitter:

    def __init__(self):
        self.tweets = []
        self.follows = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.follows:
            self.follows[userId] = {userId}
        heapq.heappush_max(self.tweets, (self.time, userId, tweetId))
        self.time += 1
        return None
    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.follows:
            return []
        snapshot = self.tweets.copy()
        feed = []
        while snapshot and len(feed) < 10:
            _, uid, tid = heapq.heappop_max(snapshot)
            if uid in self.follows[userId]:
                feed.append(tid)
            
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follows:
            self.follows[followerId] = set()
        self.follows[followerId].add(followeeId)
        return None

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follows and followeeId in self.follows[followerId] and followerId != followeeId:
            self.follows[followerId].remove(followeeId)
        return None