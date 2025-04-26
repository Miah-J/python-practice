"""
    To be honest this one was among the tricky ones. Doing a reverse without using the
    inbuilt fuction. I knew it was going to be a loop ,but I couldn't figure out how
    to do it. I thought of doing my method way ,but I decided to go direct because I
    could mess up the method. I employed a for loop.
"""
string_Im_reversing = " Data Structures And Algorithms "

"""
    This is going to hold the reversed string(It has to be empty)
"""
reversed_String = ""

"""
    And of course the for loop to loop through each character in the string.
"""
for ch in string_Im_reversing:
    """
        Now this just adds the current character in front of the reversed character  
    """
    reversed_String = ch + reversed_String

print(reversed_String)