def two_sum(nums,target):
	'''find the sum of two numbers from given list and check is equal to 
           target value or not and return list of index of that two value'''
	for i in range(len(nums)):
		if target >= nums[i]:
			val = target-nums[i]
			if (val in nums) and i != nums.index(val) and (val+nums[i] == target):
				print([i,nums.index(val)])
				break
		elif nums[i] > target:
			val = nums[i]-target
			if (val in nums) and i!=nums.index(val) and (val+nums[i] == target):
				print([i,nums.index(val)])
				break
	else:
		print("Not Found")
		
nums = []
try:
	no_of_item = int(input("Enter no of items: "))
	if no_of_item>=1:
		for i in range(no_of_item):
			item = int(input("Enter item: "))
			nums.append(item)
		target = int(input("Enter target value: "))
		two_sum(nums,target)
	else:
		print("please enter at least one items.")
except ValueError:
	print("Not valid input")
