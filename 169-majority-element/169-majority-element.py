class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate ,count = 0,0
        for i in nums:
            if i == candidate:
                count += 1
            elif count == 0:
                candidate ,count = i ,1
            else:
                count -= 1
        return candidate