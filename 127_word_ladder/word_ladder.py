# 127. Word Ladder
# Hard
# Topics
# premium lock icon
# Companies
# A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

# Every adjacent pair of words differs by a single letter.
# Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
# sk == endWord
# Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.


# Example 1:

# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
# Output: 5
# Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
# Example 2:

# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
# Output: 0
# Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.


# Constraints:

# 1 <= beginWord.length <= 10
# endWord.length == beginWord.length
# 1 <= wordList.length <= 5000
# wordList[i].length == beginWord.length
# beginWord, endWord, and wordList[i] consist of lowercase English letters.
# beginWord != endWord
# All the words in wordList are unique.

class Node:
    def __init__(self, word):
        self.word = word
        self.children = []
        self.parent = None

    def add_child(self, child):
        self.children.append(child)
        child.parent = self


def diff_counter(word1, word2):
    diffs = 0
    if len(word1) != len(word2):
        raise Exception('cannot diff words that are not equal len')
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            diffs += 1
    return diffs


def try_add_word(node, word):
    if diff_counter(node.word, word) == 1:
        n = Node(word)
        node.add_child(n)
        return n
    elif diff_counter(node.word, word) > 1:
        for child in node.children:
            n = try_add_word(child, word)
            if n:
                return n
    return None


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0
        root = Node(beginWord)
        endNode = None
        while len(wordList):
            word = wordList.pop(0)
            added = try_add_word(root, word)
            if added:
                if word == endWord:
                    endNode = added
                    break
            if not added:
                wordList.append(word)

        p = endNode
        counter = 0
        while p:
            counter += 1
            p = p.parent
        return counter


sln = Solution()
sln.ladderLength("hit", "cog", ["cog", "hot", "dot",
                 "dog", "lot", "log", "ass"])
