# This is to simulate a infinite monkey that randomly types letter #
# This program uses hill-climbing technique to reduce the iteration number #

import string
import random
def generateOne(strlen):
    """Generate a random string of length strlen with space"""
    alp_all = string.ascii_lowercase+' '
    out =''.join([random.choice(alp_all) for _ in range(strlen)])
    return out

def getScore(str_gen, str_target):
    """return a score of how well the generated string matches target"""
    N = len(str_gen)
    score = 0
    if N!=len(str_target):
        raise ValueError("%s and %s must have same length" % (str_gen, str_target))
        return score
    score = 0
    replace_index =  []
    for i in range(N):
        if str_gen[i] == str_target[i]:
            score += 1
        else:
            replace_index.append(i)
    score /= float(N)
    return score, replace_index

def updateString(str_old, str_rep, rep_index):
    str_old = list(str_old)
    for i in range(len(str_rep)):
        j = rep_index[i]
        str_old[j] = str_rep[i]
    return ''.join(str_old)

def main():
    str_target = 'methinks it is like a weasel'
    strlen     = len(str_target)
    count      = 0
    best_score = -1
    score = 0
    replace_index = list(range(strlen))
    str_gen       = generateOne(strlen) 
    while score < 1.0 - 1e-6:
        score, replace_index  = getScore(str_gen, str_target)
        str_replace = generateOne(len(replace_index))
        str_gen = updateString(str_gen, str_replace, replace_index)
        count  += 1
        if best_score<score:
            best_score = score
        if count%10== 0:
            print('%d th try,%s, best score %f.' % (count,str_gen, best_score))
    print('Done in %d iterations! %s'%(count ,str_gen))


if __name__ == "__main__":
    main()




