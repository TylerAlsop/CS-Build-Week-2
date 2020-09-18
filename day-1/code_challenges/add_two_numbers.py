# U
    # Given two linked lists containing positive numbers as nodes
    # When going through the linked list in reverse order one would produce a number that is as many digits long as there are nodeds in the linked list.
    # Need to add together the numbers that each list produces
    # Then return a linked list that is the sum of the two numbers
        # returned linked list must be in the same format as the two lists given at the begining.
        
# P
    # Create three empty arrays. One for each list given and another for the sum.
    # Create two empty strings to add the given numbers to
    # Create a new linked list to return in the end
    # Think of edge cases:
        # Empty List
        # List that is just one value
        
    # Loop over each list given. 
    # For each node in the list:
        # Append the number to its corresponding array.
    # Reverse the arrays
    # Convert each array to a single string
        # Loop over the array
        # For each num in the array:
            # Convert the num to a string
            # Add the stringified num to the corresponding empty string above
    # Convert the string to a number
    # Add the numbers
    # Convert the sum to a string
    # Loop over the string
        # For each item in the string add it to the third empty array.
    # Reverse the third array.
    # Loop over the third array.
    # For each item in the third array add it as a new node in the third list to be returned.
    # Return the third list
    
    #NOTE: May need to create helper functions to add new nodes to a list


########################### Attempt 1 ###########################
# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next

# class Solution:
#     def __init__(self):
#         self.head = None
    
#     def addNode(self, new_num)
#         new_node = ListNode(new_num)
#         new_node.next = self.head
#         self.head = new_node
    
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#         arr_1 = []
#         arr_2 = []
#         arr_3 = []
        
#         num_1 = ""
#         num_2 = ""
        
#         for item in l1:
#             arr_1.append(item)

#         for item in l2:
#             arr_2.append(item)
            
            
#         arr_1.reverse()
#         arr_2.reverse()
        
#         for item in arr_1:
#             num_string = str(item)
#             num_1 += num_string
            
#         for item in arr_2:
#             num_string = str(item)
#             num_2 += num_string
        
#         int(num_1)
#         int(num_2)
        
#         num_3 = num_1 + num_2
        
#         str(num_3)
        
#         for char in num_3:
#             char_num = int(char)
#             arr_3.append(char_num)
            
#         arr_3.reverse()
        
#         for num in arr_3:
#             self.addNode(num)
            
    
# R
    # Way over complicated. Wasn't using the linked lists properly (i.e. utilizing .val and .next)
    # After looking over possible solutions it looks like one could traverse each node of each linked list simultaneously and utilize the built in "carry" for python and it would be like doing a simple addition by hand which adds the last numbers first and carries the 1 if the sum is over 10.
    
    
    
########################### Attempt 2 ###########################

# P-2

    # Keep in mind edge cases:
        # Where linked lists aren't equal lengths
        # Empty Lists
        # When the sum of the last digits still has a carry

    # Initialize current node to dummy head of the returning list.
    # Initialize carry to 00.
    # Initialize pp and qq to head of l1l1 and l2l2 respectively.
    # Loop through lists l1l1 and l2l2 until you reach both ends.
    # Set xx to node pp's value. If pp has reached the end of l1l1, set to 00.
    # Set yy to node qq's value. If qq has reached the end of l2l2, set to 00.
    # Set sum = x + y + carrysum=x+y+carry.
    # Update carry = sum / 10carry=sum/10.
    # Create a new node with the digit value of (sum \bmod 10)(summod10) and set it to current node's next, then advance current node to next.
    # Advance both pp and qq.
    # Check if carry = 1carry=1, if so append a new node with digit 11 to the returning list.
    # Return dummy head's next node.
    # Note that we use a dummy head to simplify the code. Without a dummy head, you would have to write extra conditional statements to initialize the head's value.



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
            
            
        