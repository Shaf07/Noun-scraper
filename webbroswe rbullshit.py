import webbrowser
import random


def webSearch(customSearch):
    url = "https://www.google.co.uk/search?q="
    searchRes = url + customSearch
    webbrowser.open(searchRes)


def guessingGame():
    correct = False
    while not correct:
        actual = random.randrange(1,3)
        guess = int(input("Guess the number:  "))
        if guess == actual:
            webSearch("congrats")
            correct = True
        else:
            print(f"The number was {actual}")

class Person:
    def __init__(self, height, weight, age):
        self.height = height
        self.weight = weight
        self.age = age
    
    def returnObj(self):
        return(self.height, self.weight, self.age)

aaron = Person("174", "200", "24")
 
#print(f" Here are the stats for Aaron: {aaron.returnObj()}")


class Child(Person): 
    def __init__(self, height, weight, age, school):
        super().__init__(height, weight, age)
        self.school = school

    def returnObj(self):
        return(self.height, self.weight, self.age, self.school)

myChild = Child("123", "100", "12", "Roe Lee")

print(myChild.returnObj())