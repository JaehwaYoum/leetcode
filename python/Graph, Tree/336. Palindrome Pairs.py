# 336. Palindrome Pairs
# https://leetcode.com/problems/palindrome-pairs/

# Date: Dec 23, 2023
# Difficulty: Hard

# Solution 1: Brute Force, TLE
class Solution1(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """

        def is_palindrome(word):
            return word == word[::-1]

        result = []
        for i, word1 in enumerate(words):
            for j, word2 in enumerate(words):
                if i == j:
                    continue
                if is_palindrome(word1 + word2):
                    result.append([i, j])
        return result

# Solution 2: Trie
import collections
class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.word_id = -1
        self.palindrome_word_ids = []
class Trie:
    def __init__(self):
        self.root = TrieNode()

    @staticmethod
    def is_palindrome(word):
        return word == word[::-1]

    def insert(self, index, word):
        node = self.root

        for i, char in enumerate(reversed(word)):
            if self.is_palindrome(word[:len(word) - i]):
                node.palindrome_word_ids.append(index)
            node = node.children[char]

        node.word_id = index

    def search(self, index, word):
        result = []
        node = self.root

        for i, char in enumerate(word):
            if node.word_id >= 0 and self.is_palindrome(word[i:]):
                result.append([index, node.word_id])

            if char not in node.children:
                return result

            node = node.children[char]

        if node.word_id >= 0 and node.word_id != index:
            result.append([index, node.word_id])

        for pal_id in node.palindrome_word_ids:
            result.append([index, pal_id])

        return result


class Solution2(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        trie = Trie()

        for i, word in enumerate(words):
            trie.insert(i, word)

        results = []
        for i, word in enumerate(words):
            results.extend(trie.search(i, word))

        return results

# Test case
solution = Solution2()

words = ["abcd", "dcba", "lls", "s", "sssll"]
output = solution.palindromePairs(words)
print(output) # [[0, 1], [1, 0], [2, 4], [3, 2]]
