individual_prices = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15,
    'E': 40,
}

class Offer(object):
    def __init__(self, required, cost):
        self.required = required
        self.cost = cost

    def process(self, items, price):
        for type in individual_prices.keys():
            if self.required.get(type, 0) > items[type]:
                return items, price

        for type in individual_prices.keys():
            items[type] -= self.required.get(type, 0)

        price += self.cost

        return self.process(items, price)


offers = [
    Offer(required={'A': 5}, cost=200),
    Offer(required={'A': 3}, cost=130),
    Offer(required={'E': 2, 'B': 1}, cost=80),
    Offer(required={'B': 2}, cost=45),
]


# noinspection PyUnusedLocal
def checkout(skus):
    if not isinstance(skus, basestring):
        return -1
    items = {x: 0 for x in individual_prices.keys()}
    try:
        for x in skus:
            items[x] += 1
    except KeyError:
        return -1
    price = 0

    for offer in offers:
        items, price = offer.process(items, price)

    for item, count in items.iteritems():
        price += individual_prices[item] * count

    return price
