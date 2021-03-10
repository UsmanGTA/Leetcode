def isValid(s):
    """
    ---------------
    METHOD: isValid
    ---------------
    Description:
        This function checks whether or not
        a given string actually has valid
        parenthesis
    Args:
        @s: input string
    Return:
        None
    """
    parenthesis = {'(': ')',
                    '[': ']',
                    '{': '}'}
    parenthesis_stack = ""

    for char in s:
        if char in parenthesis:
            parenthesis_stack += char
            continue
        if char == ')' or char == ']' or char == '}':
            if parenthesis_stack != "" and parenthesis[parenthesis_stack[-1]] == char:
                parenthesis_stack = parenthesis_stack[:-1]
            else:
                return False

    return parenthesis_stack == ""


        # O(n + m)
        # Rules
        # We're going to have to keep track of
        # opened parenthesis and which ones they
        # are.

        # Opened parentheis must always be closed
        # in reverse, essentially, forming a
        # palindrome if valid, otherwise,
        # false.
        
        # O(n)
        # Rules
        # Loop through the string
        # if an opening parenthesis is found
        # go a level deeper with recursion

        # If a closing bracket is found, then,
        # return that closing bracket and
        # match them with a dictionary
        
        # If false, then return back as many stacks
        # possible and return false
        
        # Else if the closing bracket is good, then
        # from the former stack recall continue
        # from the index where the closing bracket
        # was found.
        
        # If another openining bracket wad found, add it
        # to the stack
        
        # At the null char return true