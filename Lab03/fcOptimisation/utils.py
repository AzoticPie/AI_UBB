from random import uniform

def generateNewValue(lim1, lim2):
    return int(uniform(lim1, lim2+1))

def binToInt(x):
    val = 0
    # x.reverse()
    for bit in x:
        val = val * 2 + bit
    return val