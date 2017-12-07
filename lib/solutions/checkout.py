individual_prices = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15,
}


# noinspection PyUnusedLocal
def checkout(skus):
    items = {x: 0 for x in 'ABCD'}
    try:
        for x in skus:
            items[x] += 1
    except KeyError:
        return -1
    price = 0

    while items['A'] >= 3:
        price += 130
        items['A'] -= 3

    while items['B'] >= 2:
        price += 45
        items['A'] -= 2

    for item, count in items.iteritems():
        price += individual_prices[item] * count

    return price
