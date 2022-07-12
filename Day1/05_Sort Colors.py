class Solution:
    def sortColors(self, nums: List[int]) -> None:
        left_index=0
        traversal_index=0
        right_index=len(nums)-1
        
        for i in range(len(nums)):
            if nums[traversal_index]==0:
                nums[traversal_index],nums[left_index]=nums[left_index],nums[traversal_index]
                left_index+=1
                traversal_index+=1
                
            elif nums[traversal_index]==1:
                traversal_index+=1
            else:
                nums[traversal_index],nums[right_index]=nums[right_index],nums[traversal_index]
                right_index-=1
                
                
                
