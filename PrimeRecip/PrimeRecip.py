import math
import json
from pathlib import Path

#
#   Output a list of reciprocals for the specified primes
#


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
def GetPrimeRecip(pPrime):

    if pPrime in (2, 5):
        period = 1
        output = pPrime
    else:
        period = PrimeRecipPeriod(pPrime)
        dividend = 1
        output = ""

        # Generate exactly the number of digits in the period
        for _ in range(period):
            dividend *= 10
            result = dividend // pPrime
            dividend %= pPrime
            output += str(result)

    return {"Prime:": pPrime, "Periodicity": period, "Value": f"0.{output}"}

def generate_markdown_table(pMDPath, pPrimeList):

    # header
    Header = [
        "# PrimeRecip",
        f"Reprical values of first {len(pPrimeList)} prime numbers",
        "| Num | Prime | Period Length | Decimal Sequence Preview |",
        "| :--- | :--- | :---: | :--- |"
    ]

    n = 1
    for entry in pPrimeList:
        prime = entry.get("Prime", entry.get("Prime:")) # Catches both key formats safely
        val = entry.get("Value", "")
        period = entry.get("Periodicity", 0)

        truncatedVal = f"`{val[:30]}...`" if len(val) > 30 else f"`{val}`"
        
        Header.append(f"| {n} | **{prime}** | {period} | <code>{truncatedVal}</code> |")

        n+=1


    with open(str(pMDPath), "w", encoding="utf-8") as f:
        f.writelines(f"{line}\n" for line in Header)


# Load primes
ScriptDir = Path(__file__).parent
input_file = ScriptDir / "Primes.json"

RecipList = []
with open(input_file, "r", encoding="utf-8") as f:
    for p in json.load(f):
        per = GetPrimeRecip(p)
        RecipList.append(per)

JSONOutput = ScriptDir / "PrimeRecip.json"
with open(JSONOutput, "w") as json_file:
    json.dump(RecipList, json_file, indent=4)

MDPrimeRecip = ScriptDir / "PrimeRecip.md"
generate_markdown_table(MDPrimeRecip,  RecipList)