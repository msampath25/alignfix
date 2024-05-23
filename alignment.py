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

    def output_alignment(lower, middle, upper, curr_graph, s_mod, t_mod, s, t, i, j, match_reward, mismatch_penalty, gap_opening_penalty, gap_extension_penalty):
        if i == 0 and j == 0:
            return s_mod, t_mod
        if curr_graph is lower:
            if i > 0 and lower[i][j] == middle[i - 1][j] - gap_opening_penalty:
                curr_graph = middle
            s_mod = s[i - 1] + s_mod
            t_mod = '-' + t_mod
            return output_alignment(lower, middle, upper, curr_graph, s_mod, t_mod, s, t, i - 1, j, match_reward, mismatch_penalty, gap_opening_penalty, gap_extension_penalty)
        elif curr_graph is upper:
            if j > 0 and upper[i][j] == middle[i][j - 1] - gap_opening_penalty:
                curr_graph = middle
            s_mod = '-' + s_mod
            t_mod = t[j - 1] + t_mod
            return output_alignment(lower, middle, upper, curr_graph, s_mod, t_mod, s, t, i, j - 1, match_reward, mismatch_penalty, gap_opening_penalty, gap_extension_penalty)
        else:
            if middle[i][j] == lower[i][j]:
                curr_graph = lower
                return output_alignment(lower, middle, upper, curr_graph, s_mod, t_mod, s, t, i, j, match_reward, mismatch_penalty, gap_opening_penalty, gap_extension_penalty)
            elif middle[i][j] == upper[i][j]:
                curr_graph = upper
                return output_alignment(lower, middle, upper, curr_graph, s_mod, t_mod, s, t, i, j, match_reward, mismatch_penalty, gap_opening_penalty, gap_extension_penalty)
            else:
                s_mod = s[i - 1] + s_mod
                t_mod = t[j - 1] + t_mod
                return output_alignment(lower, middle, upper, curr_graph, s_mod, t_mod, s, t, i - 1, j - 1, match_reward, mismatch_penalty, gap_opening_penalty, gap_extension_penalty)

    def affine_alignment(match_reward, mismatch_penalty, gap_opening_penalty, gap_extension_penalty, s, t):
        sl = len(s)
        tl = len(t)
        lower = np.full((sl + 1, tl + 1), 0, dtype=int)
        middle = np.full((sl + 1, tl + 1), 0, dtype=int)
        upper = np.full((sl + 1, tl + 1), 0, dtype=int)
        
        for i in range(1, sl + 1):
            upper[i][0] = -99999
            middle[i][0] = -(gap_opening_penalty + (i - 1) * gap_extension_penalty)
            lower[i][0] = -(gap_opening_penalty + (i - 1) * gap_extension_penalty)
        
        for j in range(1, tl + 1):
            upper[0][j] = -(gap_opening_penalty + (j - 1) * gap_extension_penalty)
            middle[0][j] = -(gap_opening_penalty + (j - 1) * gap_extension_penalty)
            lower[0][j] = -99999
        
        upper[0][0] = -99999
        lower[0][0] = -99999
        
        for i in range(1, sl + 1):
            for j in range(1, tl + 1):
                match = match_reward if s[i - 1] == t[j - 1] else -mismatch_penalty
                lower[i][j] = max(lower[i - 1][j] - gap_extension_penalty, middle[i - 1][j] - gap_opening_penalty)
                upper[i][j] = max(upper[i][j - 1] - gap_extension_penalty, middle[i][j - 1] - gap_opening_penalty)
                middle[i][j] = max(lower[i][j], upper[i][j], middle[i - 1][j - 1] + match)
        
        s_mod = ""
        t_mod = ""
        curr_graph = middle
        s_mod, t_mod = output_alignment(lower, middle, upper, curr_graph, s_mod, t_mod, s, t, sl, tl, match_reward, mismatch_penalty, gap_opening_penalty, gap_extension_penalty)
        
        return middle[sl][tl], s_mod, t_mod
    
    def align(self):







