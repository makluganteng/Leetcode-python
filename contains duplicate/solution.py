

# First Way (For Loop) O(n)
def containDuplicate(num):
    num.sort()
    print(num)
    for i in range(len(num)):
        if i == len(num)-1:
            return False
        elif num[i] == num[i+1]:
                return True
    return False

case1 = [1,2,3,1];
case2 = [1,1,1,3,3,4,3,2,4,2]

print(containDuplicate(case1))

#Second Way (Recursion Method) 0(1)
def containDuplicate2(nums):
    nums.sort()
    return containInner(nums, 0)
    
def containInner(nums, index):
    if index == len(nums)-1:
        return False
    elif nums[index] == nums[index+1]:
        return True
    return containInner(nums, index+1)


print(containDuplicate2(case1))
print(containDuplicate2(case2))