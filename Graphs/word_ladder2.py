# Leetcode: https://leetcode.com/problems/word-ladder-ii/description/
# https://www.youtube.com/watch?v=DREutrv2XD0


import string
from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0

        queue = deque([(beginWord, 1)])
        while queue:
            word, steps = queue.popleft()
            if word == endWord:
                return steps
            for i in range(len(word)):
                for c in string.ascii_lowercase:
                    new_word =  word[:i] + c + word[i+1:]
                    if new_word in word_set:
                        word_set.remove(new_word)
                        queue.append((new_word, steps + 1))
        return 0