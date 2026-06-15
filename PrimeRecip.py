import math
import json
from pathlib import Path
import Utils as u

#
#   Output a list of reciprocals for the specified primes
#



def MarkdownOutputPrimeRecip(pMDPath, pPrimeList):

    # header
    Header = [
        "# PrimeRecip",
        f"Reprical values of first {len(pPrimeList)} prime numbers",
        "| Num | Prime | Period Length | Decimal Sequence Preview |",
        "| :--- | :--- | :---: | :--- |"
    ]

    n = 1
    for entry in pPrimeList:
        prime = entry.get("Prime", "")
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
        perLength = u.PrimeRecipPeriod(p)
        per = u.GetPrimeRecip(p, perLength)
        RecipList.append(per)

JSONOutput = ScriptDir / "PrimeRecip.json"
with open(JSONOutput, "w") as json_file:
    json.dump(RecipList, json_file, indent=4)

MDPrimeRecip = ScriptDir / "PrimeRecip.md"
MarkdownOutputPrimeRecip(MDPrimeRecip,  RecipList)