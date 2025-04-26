"""
    Factorial with recursion I'm going with if...else and hoping it works out
    because my last factorial where I used a method did not work out and I
    failed to fix it. So I'm going to keep this one simple. Oh, yeah in recursion
    a function is basically calling itself.
"""
def recursion_factorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * recursion_factorial(x - 1)

"""
    As usual the code in action.
"""
testSubject = 5
print(f"The Factorial of {testSubject} is {recursion_factorial(testSubject)}")

"""
    This worked out well as it was more or less what we had done in java just had to
    translate it to python.
"""

