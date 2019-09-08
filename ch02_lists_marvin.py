"""Slicing lists in a for loop!"""

paranoid_android = 'Marvin The Paranoid Android'

for i, letter in enumerate(paranoid_android[:6]):
    print(' '*i, letter)

for letter in paranoid_android[-7:]:
    print('\t ', letter)

for j, letter in enumerate(paranoid_android[11:19]):
    print('\t'*j, letter)
