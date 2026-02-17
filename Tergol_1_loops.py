num = [5,2,7,9,-1,0,-5]
num.sort(reverse=True)
print(num)
num.sort(reverse=False)
print(num)

#Tergil_loops_first_option
nums = [5,2,1,9,-4,2]
for x in nums:
   if nums.count (x) > 1:
        nums.remove (x)
        nums.sort()
        print(nums)

#Tergol_loops_seacond_option
nums = [5,2,1,9,-4,2]
nums.sort()
dup = False
for number in range(len(nums)):
    if nums[number] == nums[number-1]:
        dup = True
        print (nums)

if dup == False:
    print ("No duplication")
if dup == True:
    print ("Duplication")