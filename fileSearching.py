import time


def removeArticles(file):
    print("Loading...")
    start = time.perf_counter()
    nouns = open("nouns.txt", "r")
    nounsExtract = nouns.read().split()
    text = open(f"{file}", "r", encoding="utf-8") #this is the encoding used in the txt file
    fileContents = text.read().split()
    results = []
    for i in fileContents: 
        if i in nounsExtract:
            if i not in results:
                results.append(i)
            for i in nounsExtract:
                pluralNoun = (i+"s")
                if pluralNoun in fileContents:
                    if pluralNoun not in results:
                        results.append(pluralNoun)
    print(results)
    finish = time.perf_counter()

    print(f"List of {len(results)} nouns identified in: {start - finish:0.4f} seconds")


def searchFile():
    theText = input("Type the filename here:  ")
    removeArticles(theText)

searchFile()


