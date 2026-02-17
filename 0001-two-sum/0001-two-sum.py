class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        distionary = {}
        for i,num in enumerate(nums):
            diff = target-num
            if diff in distionary:
                return [distionary[diff],i]
            
            distionary[num]=i