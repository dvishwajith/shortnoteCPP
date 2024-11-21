def romanToInt(s: str) -> int:

    one_char_dict = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000,
    }

    two_char_dict = {
        'IV' : 4,
        'IX' : 9,
        'XL' : 40,
        'XC' : 90,
        'CD' : 400,
        'CM' : 900,
    }

    def romanToIntHelper(s: str) -> int:
        if len(s) <= 0:
            return 0
        msb_val = 0
        if len(s) >= 2:
            if s[0:2] in two_char_dict:
                msb_val = two_char_dict[s[0:2]]
                return msb_val + romanToIntHelper(s[2:])

        msb_val = one_char_dict[s[0]]
        return msb_val + romanToIntHelper(s[1:])
    
    return romanToIntHelper(s)

print(romanToInt("MCMXCIV"))