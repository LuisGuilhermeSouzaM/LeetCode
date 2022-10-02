class Solution(object):
    def isAnagram(self, s, t):
        return all(s.count(_) == t.count(_) for _ in 'abcdefghijklmnopqrstuvwxzy')