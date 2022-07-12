def removeDuplicates(nums):

    k = len(set(nums))
    i = 1
    while i < k:
        if nums[i] == nums[i-1]:
            # nums[:] = nums[:i] + nums[i + 1:] + [nums[i]]
            nums.pop(i)
        else:
            i += 1

    return k

def removeD(nums):

    previous = nums[0]
    for i in range(1, len(nums)):
        if nums[i] == previous:
            temp = nums[i]
            nums.pop(i)
            nums.append(temp)
        else:
            previous = nums[i]

    return len(nums)



test = [4,4,3,3,2,1]


print(test)
# print(removeD(test))
print(removeDuplicates(test))
print(test)