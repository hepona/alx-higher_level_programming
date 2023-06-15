#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or not roman_string:
        return 0
    sum = 0
    num_rom = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50,
               'C' : 100, 'D' : 500, 'M ' : 1000}
    for c in roman_string:
        v = num_rom.get(char, 0)
        if v == 0:
            return 0
        if 
    if num_rom in (roman_string):
        sum = sum + num_rom[roman_string]
    return sum
