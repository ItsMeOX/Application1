from typing import List
from collections import defaultdict
from heapq import nsmallest, heappush

class Twitter:

    def __init__(self):
        self.followList = defaultdict(list) # followee: [follower]
        self.postList = defaultdict(list) # poster: [(time, tweetID)]
        self.day = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.postList[userId].append((-self.day, tweetId))
        self.day += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        for post in self.postList[userId]:
            heappush(res, post)
        
        for followerId in self.followList[userId]:
            for post in self.postList[followerId]:
                heappush(res, post)

        res2 = nsmallest(10, res, key=lambda e: e[0])

        return [i[1] for i in res2]
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.followList[followerId]:
            self.followList[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followList[followerId]:
            self.followList[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

class Twitter:

    def __init__(self):
        self.followList = defaultdict(list) # followee: [follower]
        self.postList = defaultdict(list) # poster: [(time, tweetID)]
        self.day = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.postList[userId].append((-self.day, tweetId))
        self.day += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        for post in self.postList[userId]:
            res.append(post)
        
        for followerId in self.followList[userId]:
            for post in self.postList[followerId]:
                res.append(post)

        res.sort()

        res2 = []

        for r in res[:10]:
            res2.append(r[1])
        
        return res2
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.followList[followerId]:
            self.followList[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followList[followerId]:
            self.followList[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)