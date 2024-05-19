import numpy as np

class SA:
    def __init__(self, db):
        """
        Constructor for Suffix Array

        Parameters
        ----------
        db : string
            the genome or database that we want to create a suffix array for
        Returns
        -------
        void
        """
        self.db = db
        self.suffix_arr = self.populate(self)

    def __populate__(self):
        """
        Creates the suffix_arr array by sorting lexicographically and returning integer positions in db

        Parameters
        ----------
        self : object

        Returns
        -------
        indices : numpy array
            An array of integers indicating the positions of suffixes in db that are lexicographically sorted
        """
        suffixes = np.zeros(len(self.db))
        indices = np.zeros(len(self.db))

        for i in range(len(self.db)):
            suffixes[i] = self.db[0+i:]

        sorted_suffixes = np.sort(suffixes)
        for i in range(len(sorted_suffixes)):
            indices[i] = len(self.db) - len(sorted_suffixes[i])

        return indices

    def __searchFirstIndex__(self, word):
        """
        Finds the first lexicographic occurrence of a pattern in the suffix_arr array

        Parameters
        ----------
        self : object
        word: string
            the l-mer keyword we are looking for in the db i.e. the seed

        Returns
        -------
        first : integer
            The position in which the first occurrence of a pattern in the suffix_arr array is found
        """
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
            return -42

    def __searchLastIndex__(self, first, word):
        """
        Finds the last lexicographic occurrence of a pattern in the suffix_arr array

        Parameters
        ----------
        self : object
        word: string
            the l-mer keyword we are looking for in the db i.e. the seed

        Returns
        -------
        last : integer
            The position in which the last occurrence of a pattern in the suffix_arr array is found
        """
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
        """
        Finds the section of the suffix array that has an instance of word

        Parameters
        ----------
        self : object
        word: string
            the l-mer keyword we are looking for in the db i.e. the seed

        Returns
        -------
        first_seed : integer
            The position in which the first occurrence of a pattern in the suffix_arr array is found
        last_seed : integer
            The position in which the last occurrence of a pattern in the suffix_arr array is found
        """
        self.db += "$"
        first_seed = self.__searchFirstIndex__(self, word)
        last_seed = self.__searchLastIndex__(self, word)
        return first_seed, last_seed





