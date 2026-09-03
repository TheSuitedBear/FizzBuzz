# Version 1 will just run on the command line.

for i in range(1, 100):
    outputLine = ""
    fizz = "Fizz"
    buzz = "Buzz"
    if i % 3 == 0:
        outputLine += fizz
    elif i % 5 == 0:
        outputLine += buzz
    else:
        outputLine = i
    print(outputLine)
    
# Trying 2 different things here, idk
    
for i in range(1, 100):
    fizz = i % 3
    buzz = i % 5
    if (fizz == 0) and (buzz == 0):
        print("FizzBuzz")
    elif (fizz == 0) and (buzz != 0):
        print("Fizz")
    elif (fizz != 0) and (buzz == 0):
        print("Buzz")
    else:
        print(i)