def merge_packages(items, limit):
# UNDERSTAND
    # Given an array of itegers
        # Each integer represents the weight of an item
    # Given a weight limit
    # Need to find the first two items in the array whose sum is equal to the limit given
    # Return an array of the two items with the heaviest item is listed first
    # If no two items exist whose sum equals the limit given then return an empty array []
    # Brute force would be nested for loops with a time complexity of n^2
# PLAN
    # Handle edge cases
        # If the length of the array given of items is less than or equal to one then return an empty array
        # If the length of the array given is equal to two and those two weights equal the limit then return [1, 0]
    # Loop over the items array
    # For item i in the array:
        # Create a variable for the index of i. Call it item_i_index
        # If the item_i_index plus 1 is less than the length if the items array 
            # Loop over the items array again starting from the item after current item to the end of the list
            # For item j in the array:
            # Create a variable for the index of j. Call it item_j_index
            
                # If the sum of item_i and item_j equal the limit then:
                    # Create a list to hold the indicies of the two items. Call it two_indicies
                    # Sort the two_indicies list from largest to smallest
                    # Return the two_indicies list
    # If none of the items sum up to the limit then return and empty array []
                    
# EXECUTE
    # if len(items) <= 1:
    #     return []
    # elif len(items) == 2:
    #     if items[0] + items[1]:
    #         return [1, 0]

    # for item_i in items:
    #     item_i_index = items.index(item_i)
    #     print(f'item_i_index: {item_i_index}')
        
    #     if item_i_index + 1 < len(items):
    #         for item_j in items[item_i_index + 1:]:
    #             item_j_index = items.index(item_j)
    #             print(f'item_j_index: {item_j_index}')
                
    #             if item_i + item_j == limit:
    #                 two_indicies = [item_i_index, item_j_index]
    #                 two_indicies.sort(reverse=True)
    #                 return two_indicies
                    
    # return []
            
            
# REFLECT
    # The above code passed 5 out of 6 tests but did not take into account that there would be more than two sets of items that equal the limit.
    # Refactor code to handle this case
    
# PLAN
    # Create an empty dictionary to hold the sum of the indicies that equal the limit as keys, and lists containing the indicies that equal the limit as values. Call it items_that_equal_limit
    # Now when two items equal the limit then add them to the items_that_equal_limit dictionary in the format stated above.
    # After looping through the given array sort the items_that_equal_limit dictionary in ascending order. This will sort them according tho the lowest sum of the two indicies of items that contain weights that add up to the limit given.
    # If the items_that_equal_limit dictionary IS empty then return an empty array.
    # If the items_that_equal_limit dictionary IS NOT empty then return the value of the first item in the dictionary.


# EXECUTE

    items_that_equal_limit = {}

    if len(items) <= 1:
        return []
    elif len(items) == 2:
        if items[0] + items[1]:
            return [1, 0]

    for item_i in items:
        item_i_index = items.index(item_i)
        print(f'item_i_index: {item_i_index}')
        
        if item_i_index + 1 < len(items):
            for item_j in items[item_i_index + 1:]:
                item_j_index = items.index(item_j)
                print(f'item_j_index: {item_j_index}')
                
                if item_i + item_j == limit:
                    indicies_sum = item_i_index + item_j_index
                    two_indicies = [item_i_index, item_j_index]
                    
                    two_indicies.sort(reverse=True)
                    
                    items_that_equal_limit[indicies_sum] = two_indicies
                    
    if len(items_that_equal_limit) == 0:
        return []
    else:
        sorted_items_that_equal_limit = sorted(items_that_equal_limit.items(), key=lambda x: x[0], reverse=False)
        for i in sorted_items_that_equal_limit:
            print(i)
            return i[1]
    
    
    
# REFLECT
    # Not having nested for loops would really speed up the time complexity.