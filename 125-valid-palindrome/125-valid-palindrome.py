class Solution:
    def isPalindrome(self, s: str) -> bool:
        res=""
        for i in s:
            if(i.isalnum()):
                res+=i
        
        rev = res[::-1]
        
        if(res.lower() == rev.lower()):
            return True
        else:
            return False