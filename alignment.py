import numpy as np

class Alignment(object):

    def __init__(self, db_truncated, query, seed, l, r):
        """
        Constructor for the Alignment class

        Parameters
        ----------
        db_truncated : string
            the genome or database that we want to align to, this should already be processed so we dont have to store
            the whole database in memory
        query : string
            the read that we will align to the database
        seed: integer
            the position of the seed in the database
        l : integer
            the length of the seed
        r: integer
            the length of the alignment window
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
        
    #We could probably get rid of this method if we were to be careful in main.py
    def __position__(self):
        """
        Seed position in the query

        Parameters
        ----------
        self : object
            the alignment object

        Returns
        -------
        i : integer
            the start position of the seed in the query
        i + self.l : integer
            the end position of the seed in the query
        """
        for i in range(len(self.query) - self.l + 1):
            if self.query[i:i + self.l] == self.db[self.seed: self.seed + self.l]:
                return i, i + self.l
    
    def __output_alignment__(self, lower, middle, upper, curr_graph, s_mod, t_mod, s, t, i, j, match_reward, mismatch_penalty, gap_opening_penalty, gap_extension_penalty):
        if i == 0 and j == 0:
            return s_mod, t_mod
        if curr_graph is lower:
            if i > 0 and lower[i][j] == middle[i - 1][j] - gap_opening_penalty:
                curr_graph = middle
            s_mod = s[i - 1] + s_mod
            t_mod = '-' + t_mod
            return self.__output_alignment__(lower, middle, upper, curr_graph, s_mod, t_mod, s, t, i - 1, j, match_reward, mismatch_penalty, gap_opening_penalty, gap_extension_penalty)
        elif curr_graph is upper:
            if j > 0 and upper[i][j] == middle[i][j - 1] - gap_opening_penalty:
                curr_graph = middle
            s_mod = '-' + s_mod
            t_mod = t[j - 1] + t_mod
            return self.__output_alignment__(lower, middle, upper, curr_graph, s_mod, t_mod, s, t, i, j - 1, match_reward, mismatch_penalty, gap_opening_penalty, gap_extension_penalty)
        else:
            if middle[i][j] == lower[i][j]:
                curr_graph = lower
                return self.__output_alignment__(lower, middle, upper, curr_graph, s_mod, t_mod, s, t, i, j, match_reward, mismatch_penalty, gap_opening_penalty, gap_extension_penalty)
            elif middle[i][j] == upper[i][j]:
                curr_graph = upper
                return self.__output_alignment__(lower, middle, upper, curr_graph, s_mod, t_mod, s, t, i, j, match_reward, mismatch_penalty, gap_opening_penalty, gap_extension_penalty)
            else:
                s_mod = s[i - 1] + s_mod
                t_mod = t[j - 1] + t_mod
                return self.__output_alignment__(lower, middle, upper, curr_graph, s_mod, t_mod, s, t, i - 1, j - 1, match_reward, mismatch_penalty, gap_opening_penalty, gap_extension_penalty)

    def __affine_alignment__(self, match_reward, mismatch_penalty, gap_opening_penalty, gap_extension_penalty, s, t):
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
        
        max_bottom_score = -99999
        mbs_index = 0
        for j in range(1, tl + 1):
            if middle[sl][j] >= max_bottom_score:
                mbs_index = j
                max_bottom_score = middle[sl][j]
        
        s_mod = ""
        t_mod = ""
        curr_graph = middle
        s_mod, t_mod = self.__output_alignment__(lower, middle, upper, curr_graph, s_mod, t_mod, s, t, sl, mbs_index, match_reward, mismatch_penalty, gap_opening_penalty, gap_extension_penalty)
        
        return max_bottom_score, s_mod, t_mod

    def __bottomAlignment__(self):
        """
        Alignment of the bottom window

        Parameters
        ----------
        self : object
            the alignment object

        Returns
        -------
        self.affine_alignment() : max score, alignment_s, alignment_t
            returns an alignment of the end of the seed to the rest of the query and the truncated database
        """
        m = self.query[self.lower_alignment:]
        n = self.db[self.seed + self.l:]

        return self.__affine_alignment__(2, 3, 5, 2, m, n)

    def __topAlignment__(self):
        """
        Alignment of the top window

        Parameters
        ----------
        self : object
            the alignment object

        Returns
        -------
        self.affine_alignment() : max score, alignment_s, alignment_t
            returns an alignment of the beginning of the query to the start of the seed and the truncated database
        """
        #might be off by one here potentially
        if self.upper_alignment == 0 or self.seed == 0:
            return 0, "", ""
        m = self.query[:self.upper_alignment]
        n = self.db[:self.seed]

        rev_m = m[::-1]
        rev_n = n[::-1]

        results = self.__affine_alignment__(2, 3, 5, 2, rev_m, rev_n)
        query_alignment = results[1][::-1]
        db_alignment = results[2][::-1]
        return results[0], query_alignment, db_alignment
    
    def Align(self):
        """
        Complete alignment of the query and database

        Parameters
        ----------
        self : object
            the alignment object

        Returns
        -------
        top : max score, alignment_s, alignment_t
            the alignment info for the top window
        bottom : max score, alignment_s, alignment_t
            the alignment info for the bottom window
        """
        top = self.__topAlignment__()
        bottom = self.__bottomAlignment__()

        query_alignment = top[1] + self.db[self.seed: self.seed + self.l] + bottom[1]
        db_alignment = top[2] + self.db[self.seed: self.seed + self.l] + bottom[2]
        score = top[0] + bottom[0]
        return score, query_alignment, db_alignment




