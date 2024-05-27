import numpy as np

"""
Scoring based on BLAST
match_reward = 2
mismatch_penalty = 3
gap_opening_penalty = 5
gap_extension_penalty = 2
"""
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
