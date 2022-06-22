import time

cool_cows = ["Winnie the Moo", "Moolan", "Milkshake", "Mooana"]
cool_sheep = ["Baaaart", "Baaaarnaby"]
cool_pigs = ["Chris P. Bacon", "Hamlet", "Hogwarts"]

cool_animals = [cool_cows, cool_sheep, cool_pigs]


def ifAdd() :
    number1 = float(input("enter number"))
    number2 = float(input("enter number"))
    result = number1 / number2
    if result > 2:
        cool_cows.append(result)
        print(cool_cows)

extendList = ["newitem1", "newItem2"]

cool_cows.extend(extendList)

#
#

animalColour = {
    "bat" : "black",
    "cat": "beige"
}

def addAnimals():
    while len(animalColour) < 4:
        animal = input("Enter animal here: ")
        colour = input("Enter colour: ")
        animalColour[animal] = colour
        cool_cows.append(animal)
        print(f"{animalColour} and cow list {cool_cows}")

def printCows():
    for cows in cool_cows:
        time.sleep(0.2)
        print(cows)

def runCalculator():
    runCalc = input("Press a key to continue or X to quit:  ")
    if str(runCalc) == "X":
        pass
    else:    
        calculator()

def calculator():
    calc1 = int(input("Enter first number:  "))
    bodmas = (input("Enter x, /, + or - to create an operation:  "))
    calc2 = int(input("Enter second number:  " ))
    if bodmas == "x":
        timesResult = calc1 * calc2
        print(timesResult)
    elif bodmas == "/":
        divResult = calc1 / calc2
        print(divResult)
    elif bodmas == "+":
        plusResult = calc1 + calc2
        print(plusResult)
    else:
        minusResult = calc1 - calc2
        print(minusResult)
    runCalculator()


def altCalculator():
    result = []
    giveResult = False
    while not giveResult:
        bodmas = (input("Enter x, /, + or - to create an operation or press '=' to get your results:  "))
        number = int(input("Enter number here:  "))
        if bodmas == "x":
            runningT = (runningTotal * number)
            runningTotal.append(result)
        elif bodmas == "/":
            runningTotal = (runningTotal / number)
            print(runningTotal)
        elif bodmas == "+":
            result.append(number)
            print(result)
        elif bodmas == "-":
            runningTotal = runningTotal - number
            print(runningTotal)
        elif bodmas == "=":
            giveResult = True
    return(result)


altCalculator()
