"""
290. Word Pattern
Easy

Favorite

Share
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.
"""

class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:     
        words = str.split(" ")
        d = dict()
        if len(words) != len(pattern):
            return False
        for w, p in zip(words, pattern):
            if w not in d.keys() and p not in d.values():
                d[w] = p
            elif w not in d.keys():
                return False
            elif p not in d.values():
                return False            
            elif d[w] != p:
                return False
        return True    
