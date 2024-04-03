nums = [4,5,6,7,0,1,2]
target = 0

print("".join([str(i) for i in nums]).find(str(target)))

nums = [0]
A=[[],nums]
for i in range(len(nums)):
    if [nums[i]] not in A:
        A.append([nums[i]])
    for j in range(i+1,len(nums)):
        if [nums[i],nums[j]] not in A:
            A.append([nums[i],nums[j]])
print(A)

a,b=2,4
print(add(a,b))