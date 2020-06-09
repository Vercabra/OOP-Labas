import Coffe as cf  # Laba 6 classes


class MyArray:
    collection = ['reserved'] * 15

    def regular_extend(self):
        if len(self.collection) > 15:
            to_extend = ['rserved'] * int(len(self.collection) * 0.3)
            self.collection.extend(to_extend)

    def c_append(self, a):  # a - is any data instead of collections
        if type(a) is list or type(a) is set or type(a) is tuple or type(a) is dict is False:
            to_append = [a]
            self.collection += to_append
            self.regular_extend()
            return self.collection
        else:
            print("invalid parameter's type")

    def c_extend(self, a):  # a - is collections
        if type(a) is list or type(a) is set or type(a) is tuple or type(a) is dict is True:
            to_append = [a]
            self.collection += to_append
            self.regular_extend()
            return self.collection
        else:
            print("invalid parameter's type")

    def c_remove(self, index):
        if type(index) is int is True:
            self.collection[index] = 'reserved'
        else:
            print('Invalid index')

    def c_pop(self, index):
        if type(index) is int is True:
            self.collection[index] = 'reserved'
            to_pop = self.collection[index]
            return to_pop
        else:
            print('Invalid index')

    def c_clear(self):
        for i in range(len(self.collection)):
            self.collection[i] = 'resrved'

    def c_count(self, string):
        amount = 0
        for i in range(len(self.collection)):
            if str(string) == self.collection[i]:
                amount+=1
        if amount != 0:
            return amount
        else:
            return 'is not in list'

    def c_copy(self):
        copied = self.collection
        return copied

    def c_reverse(self):
        temp = ['reserved']*len(self.collection)
        for i in range(len(self.collection)):
            temp[(len(self.collection)-1) - i] = self.collection[i]
        return temp

    def __init__(self, list):
        for i in range(len(list)):
            self.collection[i] = list[i]
            self.regular_extend()


arr = MyArray(cf.Wagon.goods)
a = MyArray([1, 2, 3])
print(a.c_append('23'))