def compareStrings(a, b):
    if a == b:
        return "They were equal"
    elif a == None or b == None:
        return "One or more strings had no content"
    else:
        print(getStringDifferences(a, b))
        return "They were not equal"

def getStringDifferences(inputA, inputB):
    inputAArray = inputA.split()
    inputBArray = inputB.split()
    differenceInputA = []
    differenceInputB = []
    position = 0
    for letter in inputAArray:
        if(letter != inputBArray[position]):
            differenceInputA.append({letter, position})
            differenceInputB.append({inputBArray[position], position})
        position = position+1
    return(differenceInputA, differenceInputB)
