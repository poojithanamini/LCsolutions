class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        
        a=[]
        for i in sentences:
            a.append(len([x for x in i.split(' ')]))
                
        return max(a)