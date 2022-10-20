def bin_search(arr: list[int], tar: int, left: int, right: int) -> int:
	if left <= right:
		mid = (left + right) // 2
		if arr[mid] == tar: 
			return mid
		elif arr[mid] > tar:
			return bin_search(arr, tar, left, mid-1)
		else:
			return bin_search(arr, tar, mid+1, right)
	return -1    