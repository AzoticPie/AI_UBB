from random import shuffle
from random import uniform

def generate_random_permutation(n, s, d):
    nums = list(range(n))
    #nums.remove(s)
    #nums.remove(d)
    shuffle(nums)
    return nums
    #return [s] + nums + [d]


def generate_new_value(lim1, lim2):
    return int(uniform(lim1, lim2+1))

def insertCh(new_pop, max_size, ch):
    new_pop.append(ch)
    if len(new_pop) >= max_size:
        new_pop.remove(min(new_pop))
