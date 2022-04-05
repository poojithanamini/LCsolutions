class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max=0
        for i in sentences:
            a=[x for x in i.split(' ')]
            if(len(a)>max): max=len(a)
                
        return max