vovels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']


class Symbols:
    def __init__(self, ss):
        self.symbol = ss

    def set_symbol(self):
        symbol = self.symbol
        return symbol


class Letter:
    def __init__(self, l):
        self.letter = l

    def set_letter(self):
        letter = self.letter
        return letter


class Word:
    def __init__(self, w):
        self.word = w

    def set_word(self):
        word = [i for i in self.word]
        return word


class Sentence:
    def __init__(self, s):
        self.sentence = s

    def set_sentence(self):
        sentence = self.sentence.split(' ')
        return sentence


class Text:
    def __init__(self, t):
        self.text = t

    def set_text(self):
        text = self.text.split('. ')
        return text


text = Text(input('Enter the text: '))


class Task:
    to_sent = []
    for i in text.set_text():
        sentence = Sentence(i)
        to_sent.append(sentence.set_sentence())
    to_sort = []
    for i in range(len(to_sent)):
        for j in range(len(to_sent[i])):
            if len(to_sent[i][j]) > 1 and vovels.count(to_sent[i][j][0]) != 0:
                to_sort.append(to_sent[i][j])
    splited_to_sort = []
    for i in range(len(to_sort)):
        word = Word(to_sort[i])
        splited_to_sort.append(word.set_word())
    for i in range(len(splited_to_sort)):
        splited_to_sort[i].insert(0, splited_to_sort[i][1])
        a = ''.join(splited_to_sort[i])
        splited_to_sort[i] = a
    splited_to_sort.sort()
    for i in range(len(splited_to_sort)):
        splited_to_sort[i] = splited_to_sort[i][1:]


print('Sorted words: ', Task.splited_to_sort)

