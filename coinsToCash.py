def calc_dollars(**coins):
    total = 0
    print(coins)
    for denomination, value in coins.items():
        if denomination == 'pennies':
            total += value * .01
        elif denomination == 'nickels':
            total += value * .05
        elif denomination == 'dimes':
            total += value * .1
        else:
            total += value * .25

    print(f'Your total cash is ${total}')


calc_dollars(pennies=342, nickels=9, dimes=32, quarters=4)
