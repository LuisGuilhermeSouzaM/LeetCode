class Solution(object):
    def isPalindrome(s):
        s = "".join(c for c in s if c.isalnum()).lower()
        return s == s[::-1]
        
    if __name__ == "__main__":
        s = "0P"
        print(isPalindrome(s))
