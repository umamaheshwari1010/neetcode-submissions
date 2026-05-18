class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s=[]
        for a in nums:
            if a in s:
                return True
            else:
                s.append(a)
        return False