def RomanNumerals(n: int):
    if n < 1:
        return ""
    if n >= 1000:
        return "M" + RomanNumerals(n - 1000)
    if n >= 900:
        return "CM" + RomanNumerals(n - 900)
    if n >= 500:
        return "D" + RomanNumerals(n - 500)
    if n >= 400:
        return "CD" + RomanNumerals(n - 400)
    if n >= 100:
        return "C" + RomanNumerals(n - 100)
    if n >= 90:
        return "XC" + RomanNumerals(n - 90)
    if n >= 50:
        return "L" + RomanNumerals(n - 50)
    if n >= 40:
        return "XL" + RomanNumerals(n - 40)
    if n >= 10:
        return "X" + RomanNumerals(n - 10)
    if n >= 9:
        return "IX" + RomanNumerals(n - 9)
    if n >= 5:
        return "V" + RomanNumerals(n - 5)
    if n >= 4:
        return "IV" + RomanNumerals(n - 4)
    if n >= 1:
        return "I" + RomanNumerals(n - 1)