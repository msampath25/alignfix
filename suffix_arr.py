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
        self.db = db + "$"
        self.suffix_arr = self.__populate__()

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
        
        # Suggested replacement
        """""""""""""""""""""
        suffixes = np.array([self.db[i:] for i in range(len(self.db))])
        indices = np.zeros(len(self.db), dtype=int)

        sorted_indices = np.argsort(suffixes)
        for i in range(len(sorted_indices)):
            indices[i] = sorted_indices[i]

        return indices
        """""""""""""""""""""
        
        suffixes = np.empty(len(self.db), dtype="object")
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
        high = len(self.suffix_arr) - 1
        mid = -1
        first = -42
        while low <= high:
            mid = (low + high) // 2
            if self.db[int(self.suffix_arr[mid]):int(self.suffix_arr[mid] + len(word))] == word:
                low = mid
                mid -= 1
                while self.db[int(self.suffix_arr[mid]):int(self.suffix_arr[mid] + len(word))] == word:
                    low = mid
                    mid -= 1
                first = low
                break
            elif self.db[int(self.suffix_arr[mid]):int(self.suffix_arr[mid] + len(word))] < word:
                low = mid + 1
            else:
                high = mid - 1

        if first == -42:
            return first
        elif word == self.db[int(self.suffix_arr[first]):int(self.suffix_arr[first] + len(word))]:
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
        high = len(self.suffix_arr) - 1
        mid = -1
        last = -69
        while low <= high:
            mid = (low + high) // 2
            if self.db[int(self.suffix_arr[mid]):int(self.suffix_arr[mid] + len(word))] == word:
                high = mid
                mid += 1
                if mid < len(self.suffix_arr):
                    while self.db[int(self.suffix_arr[mid]):int(self.suffix_arr[mid] + len(word))] == word and mid < len(self.suffix_arr):
                        high = mid
                        mid += 1
                last = high
                break
            elif self.db[int(self.suffix_arr[mid]):int(self.suffix_arr[mid] + len(word))] < word:
                low = mid + 1
            else:
                high = mid - 1

        if last == -69:
            return last
        if word == self.db[int(self.suffix_arr[last]): int(self.suffix_arr[last] + len(word))]:
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
        first_seed = self.__searchFirstIndex__(word)
        if first_seed == -42:
            last_seed = -69
            return first_seed, last_seed

        last_seed = self.__searchLastIndex__(first_seed, word)
        return first_seed, last_seed





