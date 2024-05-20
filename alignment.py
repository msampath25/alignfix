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

    def __init__(self, db):
        self.db = db
    def align(self, seed, l, r):
        str = "bing bong"

        #I want to make an alignment






