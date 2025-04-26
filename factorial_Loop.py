"""
    My thinking here is just simple. Based on previous experiences with factorial in java
    im going to use the for loop because it's kinda easy to manipulate, and I'm used
    to it at least in terms of factorial.
"""
def factorial_loop(x):
    beginning = 1
    for i in range(1, x + 1):
        beginning = beginning * i
    return beginning

"""
    (1 , x +1) I attempted to use x++ but it kinda failed so i just went the normal way
    And now the code in action. 
"""
testSubject = 6
print(f" The Factorial of {testSubject} is {factorial_loop(testSubject)}")

"""
Can't quite get it to work yet. Push to later. Nope lemme try a different approach.
Since I can't seem to work out my method I'll just go direct then. I did later
figure out the issue was indentation with the return(apparently my return was still
in the loop) so I'm keeping the code as
a remainder after I have made the correction, but I still did a direct way below:
"""
n = 8
fact = 1

for i in range(1, n+1):
    fact = fact * i

print("The factorial of" ,(n) ,"i s ", (fact))



