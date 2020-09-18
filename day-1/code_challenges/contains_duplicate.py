# U
    # Given an array of ints
    # Need to find out if the array has any duplicate ints
        # If there are duplicates then return True
        # If not then return false
        
# P
    # Create a empty set that will contain ints
    # Create a for loop to loop over the array.
    # For each item in the array:
        # If the item is not in the set then add it.
        # If it is in the set then return true.
    # After looping through the array, if it didn't return true then return false
    
# E
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        each_num = set()
        for num in nums:
            if num not in each_num:
                each_num.add(num)
            else:
                return True
        return False
    
# R
    # Original attempt:
        # Runtime: 128 ms, faster than 70.76% of Python3 online submissions for Contains Duplicate.
        # Memory Usage: 19.1 MB, less than 68.15% of Python3 online submissions for Contains Duplicate.
        
    # Possible ways to make it run faster or use less memory:
        # Use nums.remove(num) function inside the for loop. Then if the array still has anything in it, return True, else return False
        
    
# E-2
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         each_num = set()
#         for num in nums:
#             nums.remove(num)
#             if len(nums) > 0:
#                 return True

#         return False

# R-2 
    # Did not work