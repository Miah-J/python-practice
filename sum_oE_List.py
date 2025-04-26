"""
    So basically I'm going with the for loop because I think that's the easiest
    and simplest way to go and I have done it before in java.
"""
def listOfNumbers(numbers):
    begining = 0
    for Numbers in numbers:
        begining += Numbers #So im just adding a number to the begining
    return begining #Now I'm getting back the new begining

"""
    So now I'm putting it in like an actual running thing. I'm not sure 
    if we are supposed to go this route but yeah this is an actual example
    part
"""
theActualNumbers = [9, 8, 7, 6, 5, 4] #I'm trying to be a bit unique so going backwards
print("The sum of numbers in the list is ",listOfNumbers(theActualNumbers))
