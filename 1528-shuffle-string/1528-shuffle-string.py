class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res=''
        for i in range(len(s)):
            index = indices.index(i)
            res=res+str(s[index])
        return res