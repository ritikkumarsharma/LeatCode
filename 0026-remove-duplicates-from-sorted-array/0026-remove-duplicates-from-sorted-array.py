class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #  Second way to submit code 

        n = len(nums)
        j = 1
        for i in range (1, n):
            if nums[i] != nums[i-1]:
                nums[j] = nums[i]
                j +=1
        return j