class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = {}
        for i in range(len(nums)):
            comp = target-nums[i]
            if comp in a:
                return [a[comp],i]
            else:
                a[nums[i]]=i
