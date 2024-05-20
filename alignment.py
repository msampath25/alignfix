import numpy as np

"""
Goals: Create some sort of alignment given a predetermined l-mer match 

Definitions: 
    - We need to define some sort of metric for how large our matrix is gonna be. For a string of size 150, maybe
      we only want an alignment that's size 200. 
    - We need to define some sort of scoring parameter for our alignment. Do some research on how BLAST does it
    - Do we want to implement affine gap penalties for our alignment? -> I think we should!
    - Do we want to make a banded alignment? -> This will be rather difficult, although we could just do it without
      making memory considerations
    
"""
class Alignment(object):

    def __init__(self, db_truncated, query, seed, l, r):
        """
        Constructor for the Alignment class

        Parameters
        ----------
        db_truncated : string
            the genome or database that we want to align to, this should already be processed so we dont have to store
            the whole databse in memory
        query : string
            the read that we will align to the database
        Returns
        -------
        void
        """
        self.db = db_truncated
        self.query = query
        self.seed = seed
        self.l = l
        self.r = r
        self.upper_alignment, self.lower_alignment = self.__position__()



    def __position__(self):
        for i in range(len(self.query) - self.l + 1):
            if self.query[i:i + self.l] == self.db[self.seed: self.seed+self.l]:
                return i, i + self.l


    def __bottomAlignment__(self):
        n = self.db[self.seed:]
        m = self.query[self.lower_alignment:]
        dp = np.zeros([len(m) + 1, len(n) + 1])

        for i in range(1 , len(m) + 1):
            dp[i][0] = dp[i-1][0] - 1

        for j in range(1, len(n) + 1):
            dp[0][j] = dp[0][j-1] -1

        #I have to define a scoring function
        for i in range(1, len(n) + 1):
            for j in range(1, len(n) + 1):
                dp[i][j] = 1

    def align(self):







