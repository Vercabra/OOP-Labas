import Coffe as cf  # Laba 6 classes


class MyArray:
    collection = ['reserved'] * 15

    def extend(self):
        to_extend = ['rserved'] * int(len(self.collection) * 0.3)
        self.collection.extend(to_extend)

    def __init__(self):
        for i in cf.Wagon.goods:
            self.collection.append(i)
            if len(self.collection) > 15:
                self.extend()


arr = MyArray()
print(arr.collection)