"""
    For this question I did some research and there are different ways to approach it.
    You can use a loop, recursion or the map() function. I went with the map function
    because it seemed really easy to me.
"""
the_Number = 8888

sum = sum(map(int, str(the_Number)))
"""
    str(the_Number) - This converts the number into a string. Now i have:
                '1', '2'... etc
    map(int, str(the_Number)) - This means I'm applying integers to the strings 
    and I return to integers again. This are separate integers not one whole number.
    sum(map(int, str(the_Number))) - The sum now adds up all the integers  produced
    and I print my results. 
"""
print(sum)