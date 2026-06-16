''''
   Machin's Formula

    pi / 4 = 4arctan(1/5) - arctan(1/239)

    (a / b) ^ n = a^n / b^n

    (1 / 5) ^ 5 = 1 ^ 5 / 5 ^ 5 = 1 / 3125

    arctanX = (x^1 / 1) - (x^3 / 3) + (x^5 / 5)

    if x = 1/5

    arctan (1/5) = (1/5^ 1 / 1) - (1/5^3 / 3) + (1/5^5 / 5)

                 = ((1 / 5)) / 1  - (1 / 125) / 3 + (1 / 3125) / 5

                 = (1 / 5) -  (1 / 375) +  (1 / 15625)

                       1        5       1       1       1
    (1 / 3125) / 5 = ----  /  ----- = ----  * ---- =  -----
                     3125       1     3125      5     15625


https://www.youtube.com/watch?v=t5XOXQqsTvM&t=781s           

    18:04

https://quicklatex.com


https://wch.github.io/latexsheet/latexsheet-1.png


https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions

'''

def ArchTangentSeries (p):
    
    for k in range(0, p):
