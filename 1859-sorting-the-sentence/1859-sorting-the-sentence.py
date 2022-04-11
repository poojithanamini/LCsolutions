class Solution:
    def sortSentence(self, s: str) -> str:
        low = []
        lon = []
        for word in s.split():
            low.append(word[:len(word)-1])
            lon.append(int(word[len(word)-1:]))
            
        rlist = []
        for i in range(len(lon)):
            rlist.append("")
            
        for i in range(len(low)):
            rlist[lon[i]-1] = low[i]
            
        return " ".join(rlist)