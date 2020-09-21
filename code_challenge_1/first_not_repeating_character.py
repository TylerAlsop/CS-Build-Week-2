def first_not_repeating_character(s):
# UNDERSTAND
    # Given a string of small English letters
    # Need to check for any letters that repeat
    # Of any letters that do not repeat in the string return the first one that occcurs in the string
    # If all of the characters in the string are duplicated then return the string '_'
# PLAN
    # Create an empty list to hold each character from the string. Call it string_characters.
    # Create an empty list to hold duplicate characters from the string. Call it duplicate_string_characters.
    # Create an empty list to hold characters from the string that have been verified to only occur once. Call it for_sure_one_instance.
    # Handle edge cases:
        # If the input has a length of zero then return.
        # If the input only has a length of one then return the input
    # Loop over the string
        # If an item IS NOT in the string_characters
            # Add it to the string_characters
        # If it IS in the string_characters and IS NOT in the duplicate_string_characters:
            # Add it to the duplicate_string_characters
    # Loop over the string_characters
        # If the character in string_characters IS NOT in duplicate_string_characters:
            # Add it to the for_sure_one_instance list
            
    # If the length of the for_sure_one_instance list is zero then return the string '_'
    # Otherwise return the first item in the for_sure_one_instance list
# EXECUTE
    string_characters = []
    duplicate_string_characters = []
    for_sure_one_instance = []
    
    if len(s) == 0:
        return
    elif len(s) == 1:
        return s
    
    for char in s:
        if char not in string_characters:
            string_characters.append(char)
        else:
            if char not in duplicate_string_characters:
                duplicate_string_characters.append(char)
            
    print(f'string_characters: {string_characters}')
    print(f'duplicate_string_characters: {duplicate_string_characters}')
    
    
    for item in string_characters:
        if item not in duplicate_string_characters:
            for_sure_one_instance.append(item)
            
    print(f'for_sure_one_instance: {for_sure_one_instance}')
    
            
    if len(for_sure_one_instance) == 0:
        return '_'
    else: 
        return for_sure_one_instance[0]


# REFLECT
    # I think that using other data types could help speed up the time complexity