def count():

    x = 1

    while x < 5:
        print("Turkey")
        print("Ratchelor")
        x = x + 1


count()

def countTwo():

    x = 1

    while x <= 10:
        x = x + 1
        if x % 2 == 0:
            print(x)
            print("is an even number")
        else:
            print(x)
            print("is an odd number")
        

        
countTwo() 

myWord = "bulgaria"

print(myWord[0])

def firstLetter(w):
    return w[5]

print(firstLetter("no more fortnite"))


def lastLetter(w):
    return w[len(w) - 1]

print(lastLetter("Hippo Campus"))


def spellingBee(w):
    
    x = 0
    
    while x < len(w):
        print(w[x])
        x = x + 1
    
spellingBee("dogfood")
