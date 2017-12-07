
individual_prices = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15,
    'E': 40,
    'F': 10,
    'G': 20,
    'H': 10,
    'I': 35,
    'J': 60,
    'K': 70,
    'L': 90,
    'M': 15,
    'N': 40,
    'O': 10,
    'P': 50,
    'Q': 30,
    'R': 50,
    'S': 20,
    'T': 20,
    'U': 40,
    'V': 50,
    'W': 20,
    'X': 17,
    'Y': 20,
    'Z': 21,
}

class Offer(object):
    def __init__(self, required, cost, type='normal', total_count=0):
        self.required = required
        self.cost = cost
        self.type = type
        self.total_count = total_count

    def process(self, items, price):
        if self.type == 'normal':
            return self.process_normal(items, price)
        elif self.type == 'group':
            return self.process_group(items, price)

    def process_normal(self, items, price):
        for type in individual_prices.keys():
            if self.required.get(type, 0) > items[type]:
                return items, price

        for type in individual_prices.keys():
            items[type] -= self.required.get(type, 0)

        price += self.cost

        return self.process(items, price)

    def process_group(self, items, price):
        sorted_required = sorted(self.required, key=individual_prices.get, reverse=False)
        item_count = 0
        for type in sorted_required:
            item_count += items[type]

        if item_count < self.total_count:
            return items, price
        num_required = self.total_count
        for type in sorted_required:
            print self.required
            print sorted_required
            number = min(items[type], num_required)
            num_required -= number
            items[type] -= number

        price += self.cost
        return self.process(items, price)


offers = [
    Offer(required='STXYZ', cost=45, type='group', total_count=3),
    Offer(required={'A': 5}, cost=200),
    Offer(required={'A': 3}, cost=130),
    Offer(required={'E': 2, 'B': 1}, cost=80),
    Offer(required={'B': 2}, cost=45),
    Offer(required={'F': 3}, cost=20),
    Offer(required={'H': 10}, cost=80),
    Offer(required={'H': 5}, cost=45),
    Offer(required={'K': 2}, cost=120),
    Offer(required={'N': 3, 'M': 1}, cost=120),
    Offer(required={'P': 5}, cost=200),
    Offer(required={'R': 3, 'Q': 1}, cost=150),
    Offer(required={'Q': 3}, cost=80),
    Offer(required={'U': 4}, cost=120),
    Offer(required={'V': 3}, cost=130),
    Offer(required={'V': 2}, cost=90),
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