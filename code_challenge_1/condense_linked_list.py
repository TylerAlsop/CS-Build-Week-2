# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def condense_linked_list(node):

# UNDERSTAND
    # Given a linked list. Example shows a linked list of numbers but the directions just says that it contains values.
    # Need traverse the linked list and remove any nodes that have already occured in the list, updating the list.
    # Need to return the head of the updated list.
    
# PLAN
    # Create a variable to hold values of visited nodes. Probably an empty dictionary or set
    # Create a variable for the head and save the passed in node to it
    # Create a variable for previous node and save the head to it
    # Create a variable for the current node and also save the head to it
    # Handle edge cases
        # If node is None then return
        # If there is only one node then return the node 
    # Traverse the linked list
        # While node does not equal None
            # If the value of the node IS NOT in the visited nodes:
                # Add it to the visited nodes and move to the next one.
            # If the value of the node IS in the visited nodes: 
                # Remove it from the linked list
                    # previous.next = current.next
            # Return the head of the linked list.
    
# EXECUTE
    visited_nodes = set()
    head = node
    prev_node = head
    current_node = head
    
    if node == None:
        return
    elif node.next == None:
        return node
    while current_node is not None:
        if current_node.value not in visited_nodes:
            visited_nodes.add(current_node.value)
            prev_node = current_node
            current_node = current_node.next
        else:
            prev_node.next = current_node.next
            current_node = current_node.next
    return head
    
    
# REFLECT
    # So far I feel really good about this solution. It feels short, simple, and time efficient.
    # Due to concern for time to finish all three challenges I will try to do a more in depth reflection later.