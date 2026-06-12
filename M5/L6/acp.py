class RomanNumeral:
    def convert(self, num):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4, 1
        ]

        sym = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV", "I"
        ]

        roman = ""

        for i in range(len(val)):
            while num >= val[i]:
                roman += sym[i]
                num -= val[i]

        return roman


# Input from user
number = int(input("Enter an integer: "))

obj = RomanNumeral()
print("Roman Numeral:", obj.convert(number))