class Solution:
    def isPalindrome(self, s: str) -> bool:
        def preprocess(c):
            if c.isalnum():
                return c.lower()
            else:
                return None
                
        l = 0
        r = len(s) - 1

        while l < r:
            lchar = preprocess(s[l])
            if not lchar:
                l += 1
                continue
            rchar = preprocess(s[r])
            if not rchar:
                r -= 1
                continue
            if lchar != rchar:
                return False
            else:
                l += 1
                r -= 1
        return True


        

        