import math

#   Get divisors for specified number
def GetDivisors(pNumber):
    divs = []

    n = math.isqrt(pNumber)

    for x in range(1, n+1):
        if pNumber % x == 0:
            divs.append(x)
            divs.append(pNumber // x)
    divs.sort()

    return divs

#   Calculate the period of repeating digits for the specified prime
def PrimeRecipPeriod(pPrime):
    # need special handling for 2,5
    for x in GetDivisors(pPrime - 1):
        y = pow(10,x, pPrime)
        if y == 1:
           return int(x)
        
    return pPrime - 1

#   Get the recipocal as a specified prime
def GetPrimeRecip(pPrime, pPeriodLength):

    if pPrime in (2, 5):
        period = 1
        output = pPrime
    else:
        period = pPeriodLength
        dividend = 1
        output = ""

        # Generate exactly the number of digits in the period
        for _ in range(period):
            dividend *= 10
            result = dividend // pPrime
            dividend %= pPrime
            output += str(result)

    return {"Prime:": pPrime, "Periodicity": period, "Value": f"0.{output}"}



print(GetPrimeRecip(2555,100))
print(GetPrimeRecip(375,100))
print(GetPrimeRecip(15625,100))
print(GetPrimeRecip(546875,100))


'''
The Rule for StoppingA fraction will always turn into a terminating decimal if its denominator's prime factors are only 2s, 5s, or both.


'''