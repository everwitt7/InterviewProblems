# https://leetcode.com/problems/palindrome-number/
def isPalindrome(num: int) -> bool:
	if num < 0: return False

	digits = [int(n) for n in str(num)]
	left, right = 0, len(digits) - 1

	while left < right:
		if digits[left] != digits[right]:
			return False
		left += 1
		right -= 1
	return True