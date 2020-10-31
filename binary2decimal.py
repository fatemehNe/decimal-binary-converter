
def UbinaryToDecimal(num, intSize, fracSize):  #num must be string
    res = 0
    intpart = num[0:intSize]
    fracpart = num[intSize: intSize + fracSize]

    for i in range(intSize):
        if intpart[i] == "1":
            res += 2**(intSize-i-1)

    for i in range(fracSize):
        if fracpart[i] == "1":
            res += 2**(-1*(i+1))
    return res

def SbinaryToDecimal(num, intSize, fracSize):
    binary = ""

    if (num[0] == "0"):
        res = UbinaryToDecimal(num[1 : intSize + fracSize], intSize-1, fracSize)
        return(res)
    elif (num[0] == "1") :
        for i in range(len(num)):
            if (num[i] == "1"):
                binary += "0"
            elif (num[i] == "0"):
                binary += "1"
        x = True
        i = len(num) - 1
        while(x):
            if (binary[i] == "0"):
                if (i == len(num) - 1):
                    Nbinary = binary[0 : i] 
                    Nbinary += "1"
                elif (i < len(num) - 1):
                    Nbinary = binary[0 : i] 
                    Nbinary += "1"
                    Nbinary += binary[i+1 : len(num) ] 
                x = False
            elif (binary[i] == "1"):
                if (i == len(num) - 1):
                    Nbinary = binary[0 : i] 
                    Nbinary += "0"
                elif (i < len(num) - 1):
                    Nbinary = binary[0 : i] 
                    Nbinary += "0"
                    Nbinary += binary[i+1 : len(num) ] 
                i -= 1
            binary = Nbinary
        res = UbinaryToDecimal(Nbinary, intSize, fracSize)
        return(res*-1 )