# Leetcode: https://leetcode.com/problems/design-twitter/

# https://www.youtube.com/watch?v=pNichitDD2E


from collections import defaultdict
import heapq


class Twitter:

    def __init__(self):
        self.count = 0
        self.follow_map = defaultdict(set)
        self.tweet_map = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_map[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> list[int]:
        res = []
        min_heap = []

        self.follow_map[userId].add(userId)
        for followee_id in self.follow_map[userId]: # O(k)
            if followee_id in self.tweet_map:
                index = len(self.tweet_map[followee_id]) - 1
                count, tweet_id = self.tweet_map[followee_id][index]
                min_heap.append([count, tweet_id, followee_id, index - 1])

        heapq.heapify(min_heap)  # O(k)
        
        while min_heap and len(res) < 10: # O(10 * logk)
            count, tweet_id, followee_id, index = heapq.heappop(min_heap)
            res.append(tweet_id)
            if index >= 0:
                count, tweet_id = self.tweet_map[followee_id][index]
                heapq.heappush(min_heap, [count, tweet_id, followee_id, index - 1])
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follow_map[followerId]:
            self.follow_map[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)