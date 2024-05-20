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
class Alignment:

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


    def

    def align(self):
        # I want to make an alignment of bottom and then upper
        # Then concatenate all alignments in the following wat upper + (seed) + bottom

        #I want to make an alignment






