def UdecimalToBinary(num, intSize, fracSize) : 

	binary = "" 

	Integral = int(num) 
	fractional = num - Integral 

	if ( Integral == 0):
		binary = "0"
	# integral to binary
	while (Integral) :
		rem = Integral % 2
		# Append 0 in binary 
		binary += str(rem); 
		Integral //= 2
	
	# Reverse string to get original binary equivalent 
	binary = binary[ : : -1] 
	temp = ""
	if ( len(binary) < intSize):
		for i in range(( intSize - len(binary) )):
			temp += "0"
		binary = temp + binary
	# binary += '.'

	# fration to binary
	while (fracSize) : 
		# Find next bit in fraction 
		fractional *= 2
		fract_bit = int(fractional) 

		if (fract_bit == 1) : 
			fractional -= fract_bit 
			binary += '1'
		else : 
			binary += '0'
		fracSize -= 1

	return binary 

def SdecimalToBinary(num, intSize, fracSize) : 
    binary = ""
    if (num >= 0) :
        return UdecimalToBinary(num, intSize, fracSize)
    else :
        temp = UdecimalToBinary(abs(num), intSize, fracSize)
        for i in range(len(temp)):
            if (temp[i] == "1"):
                binary += "0"
            elif (temp[i] == "0"):
                binary += "1"
        x = True
        i = len(temp) - 1
        while(x):
            if (binary[i] == "0"):
                if (i == len(temp) - 1):
                    Nbinary = binary[0 : i] 
                    Nbinary += "1"
                elif (i < len(temp) - 1):
                    Nbinary = binary[0 : i] 
                    Nbinary += "1"
                    Nbinary += binary[i+1 : len(temp) ] 
                x = False
            elif (binary[i] == "1"):
                if (i == len(temp) - 1):
                    Nbinary = binary[0 : i] 
                    Nbinary += "0"
                elif (i < len(temp) - 1):
                    Nbinary = binary[0 : i] 
                    Nbinary += "0"
                    Nbinary += binary[i+1 : len(temp) ] 
                i -= 1
            binary = Nbinary
        return Nbinary
