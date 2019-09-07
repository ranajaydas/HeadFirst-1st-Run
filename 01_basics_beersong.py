"""It's the '99 bottles of beer' song y'all!"""
bottle_word = 'bottles'

for beer_num in range(99, 0, -1):
    print('{} {} of beer on the wall,'.format(beer_num, bottle_word))
    print('{} {} of beer,'.format(beer_num, bottle_word))
    print('Take one down and pass it around,')

    if beer_num == 1:
        print('No more bottles of beer on the wall!')
    else:
        new_num = beer_num-1
        if new_num == 1:
            bottle_word = 'bottle'
        print('{} {} of beer on the wall!'.format(new_num, bottle_word))
    print()
