"""
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.
"""


def isAnagram(s: str, t: str) -> bool:
    if sorted(s) == sorted(t):
        return True
    else:
        return False
