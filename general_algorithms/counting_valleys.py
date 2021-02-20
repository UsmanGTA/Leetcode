#!/usr/bin/python3

def countingValleys(steps, path):
    """
    -----------------------
    METHOD: countingValleys
    -----------------------
    Description:
        Counts the number of valleys as described by
        D's and U's defined in path

        Credits:
        https://www.hackerrank.com/challenges/counting-valleys
    Args:
        @steps: len(path)
        @path: string containing D's and U's (e.g "DDUUDDUDUDU")
    """

    level = 0           # Keep track of the level
    valleycount = 0     # Store the number of valleys
    
    # Since we're keeping a track of what level we're at
    # Once it goes down, we could simply look for when
    # it comes back up, once its level, check why its level
    # if its level and it became level because of a 'u' check
    # count it as a valley
    for char in path:
        if char == "D":
            level -= 1
        else:
            level += 1

        if level == 0 and char == 'U':
            valleycount += 1

    return valleycount