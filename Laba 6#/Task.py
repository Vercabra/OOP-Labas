class Coffee:
    def __init__(self, so, w, st, p):
        self.sort = so
        self.weight = w  # in kilogram
        self.state = st
        self.price = p  # usd per kilogram

    def calc_quality(self):
        return round(self.price / self.weight, 2)


Arabic = Coffee('Arabic', 123, 'In seed', 27)
Rabusta = Coffee('Rabusta', 89, 'Blended', 21)
Liberico = Coffee('Liberico', 173, 'Canned', 45)
Exscelsa = Coffee('Exscelsa', 130, 'Packaged', 56)

wagon_goods = [Arabic.sort, Rabusta.sort, Liberico.sort, Exscelsa.sort]
wagon_total_price = 0
for i in wagon_goods:
    exec('wagon_total_price += ' + i + '.weight')
print(wagon_goods)
print(wagon_total_price)



