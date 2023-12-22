# 208. Implement Trie (Prefix Tree)
# https://leetcode.com/problems/implement-trie-prefix-tree/

# Date: Dec 18, 2023
# Difficulty: Medium

import collections
class TrieNode:
    def __init__(self):
        self.word = False
        self.children = collections.defaultdict(TrieNode)

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        node = self.root
        for char in word:
            node = node.children[char]
        node.word = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.word

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

# Test case
obj = Trie()
obj.insert("apple")

result1 = obj.search("apple")
result2 = obj.search("app")

# Checking if a word with a given prefix exists
result3 = obj.startsWith("app")
result4 = obj.startsWith("ban")

# Printing the results
print(result1)  # True
print(result2)  # False
print(result3)  # True
print(result4)  # False