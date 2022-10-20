# https://leetcode.com/problems/two-sum/
def twoSum(nums: list[int], target: int) -> list[int]:
	sol = {}
	for idx, num in enumerate(nums):
		if num in sol:
			return [idx, sol[num]]
		sol[target - num] = idx
	return -1