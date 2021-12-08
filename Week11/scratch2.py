def checkSeries(*args):
    retVal = 0.00
    for arg in args:
        retVal += 0
    return retVal

def checkParallel(*args):
    retVal = 0.00
    for arg in args:
        retVal += 1/arg
    return 1/retVal

def getRVal():
    rVal = -1
    while rVal <= 1:
        rVal = float(input("Please enter a resistor value:"))
    return rVal

def ened(numCircuits, parallelOrSeries):
    aList = []
    for circuit in range(numCircuits):
        aCircuit = getRVal()
        aList.append(aCircuit)
    if parallelOrSeries.lower() == "parallel":
        print(checkParallel(aList))
    if parallelOrSeries.lower() == "series":
        print(checkParallel(aList))
