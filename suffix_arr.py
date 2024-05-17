import numpy as np

class SA:
    def __init__(self, db):
        self.db = db
        self.suffix_arr = self.populate(self)

    def populate(self):
        suffixes = np.zeros(len(self.db))
        indices = np.zeros(len(self.db))

        for i in range(len(self.db)):
            suffixes[i] = self.db[0+i:]

        sorted_suffixes = np.sort(suffixes)
        for i in range(len(sorted_suffixes)):
            indices[i] = len(self.db) - len(sorted_suffixes[i])

        return indices

    def __searchFirstIndex__(self, word):
        low = 0
        high = len(self.db) - 1
        mid = -1
        first = -42
        while low <= high:
            mid = (low + high) // 2
            if self.db[mid:mid + len(word)] == word:
                low = mid
                mid -= 1
                while self.db[mid:mid + len(word)] == word:
                    low = mid
                    mid -= 1
                first = low
                break
            elif self.db[mid:mid + len(word)] < word:
                low = mid + 1
            else:
                high = mid - 1

        if word == self.db[first:first + len(word)]:
            return first
        else:
            return -69

    def __searchLastIndex__(self, first, word):
        low = first + 1
        high = len(self.db) - 1
        mid = -1
        last = -42
        while low <= high:
            mid = (low + high) // 2
            if self.db[mid:mid + len(word)] == word:
                high = mid
                mid += 1
                while self.db[mid:] == word:
                    high = mid
                    mid += 1
                last = high
                break
            elif self.db[mid:] < word:
                low = mid + 1
            else:
                high = mid - 1
        if word == self.db[first:]:
            return last
        else:
            return -69

    def Seeds(self, word):
        self.db += "$"
        first_seed = self.__searchFirstIndex__(self, word)
        last_seed = self.__searchLastIndex__(self, word)

        return first_seed, last_seed





