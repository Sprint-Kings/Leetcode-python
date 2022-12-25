nums = [0,0,0,1,1,2,3,4]
for i in range(len(nums)):
  for j in range(i,len(nums)-1):
    if  nums[j+1]==nums[i]:
      nums[j+1]='_'
print(nums)
k=0
for i in range(len(nums)):
  if nums[i]!='_':
    b=i
    k+=1
  for j in range(i+1,len(nums)):
    if nums[j]!='_':
      nums[b+1]=nums[j]
      if j!=(b+1):
        nums[j]='_'
      break
print(k,nums)

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            for j in range(i,len(nums)-1):
                if  nums[j+1]==nums[i]:
                    nums[j+1]='_'
        k=0
        for i in range(len(nums)):
            if nums[i]!='_':
                b=i
                k+=1
            for j in range(i+1,len(nums)):
                if nums[j]!='_':
                    nums[b+1]=nums[j]
                if j!=(b+1):
                    nums[j]='_'
                break
        return(k)