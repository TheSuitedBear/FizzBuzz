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
    
