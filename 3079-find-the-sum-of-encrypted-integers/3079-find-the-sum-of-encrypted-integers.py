class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        def calc(nums, i, n):
            if i == 0:
                return int(sorted(str(nums[0]))[-1] * len(str(nums[0])))
            return int(sorted(str(nums[i]))[-1] * len(str(nums[i]))) + calc(
                nums, i - 1, n
            )

        return calc(nums, len(nums) - 1, len(nums))
