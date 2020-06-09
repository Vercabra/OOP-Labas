class Coffe:
    def __init__(self, s, w, p, t):
        self.sort = s
        self.weight = w
        self.price = p
        self.tare = t


class Blended(Coffe):
    def __init__(self, s, w, p, t, g):
        Coffe.__init__(self, s, w, p, t)
        self.state = 'blended'
        self.grinding = g  # Grind's size


class Seeds(Coffe):
    def __init__(self, s, w, p, t, sz, d):
        Coffe.__init__(self, s, w, p, t)
        self.state = 'in seeds'
        self.size = sz  # Seed's sizes
        self.defected = d  # Defected seeds in %


class Instant(Coffe):
    def __init__(self, s, w, p, t, dm):
        Coffe.__init__(self, s, w, p, t)
        self.state = 'instant'
        self.drying_method = dm


Arabic = Blended('Arabic', 1.45, 35, 'Can', 'Coarse')
Rabusta = Seeds('Rabusta', 5, 20, 'Pocket', 'Huge', 4)
Liberico = Instant('Liberico', 200, 15000, 'Stick', 'Freeze dried')
Exscelsa = Instant('Exscelsa',  3, 65, 'Stick', 'Sublimed')

class Wagon:
    goods = [Arabic.sort, Rabusta.sort, Liberico.sort, Exscelsa.sort]

    def calc_price(self):
        price = 0
        for i in self.goods:
            price += eval(str(i)+'.price')
        return price

    def sort_quality(self):
        goods_quality = []
        for i in self.goods:
            goods_quality.append((int(int(eval((str(i)+'.price'))/int(eval((str(i)+'.weight'))))), i))
        goods_quality.sort()
        return goods_quality

w = Wagon()


