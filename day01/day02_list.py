nums = [1, 2, 3]
nums_copy = nums
nums_copy.append(4)
print(nums)
print(nums_copy)

nums2 = [ 1 , 2 , 3 ]
nums2_copy = nums2[:] # 切片拷贝
nums2_copy.append(4)
print(nums2)
print(nums2_copy)


nums3 = [ 1 , 2 , 3 ]
nums3_copy = list (nums3)
nums3_copy.append(4)
print(nums3)
print(nums3_copy)