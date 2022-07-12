def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    res = 0
    previous = roman_dict[s[0]]
    for sub in s:
        if roman_dict[sub] > previous:
            res = res + roman_dict[sub] - 2 * previous
        else:
            res += roman_dict[sub]

        previous = roman_dict[sub]

    return res

test = 'CDICIX'

print(romanToInt(test))