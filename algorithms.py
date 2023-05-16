from math import sqrt, ceil
import random
m = 10000


def first_alg(seed, s):  # linear
    a = 431
    c = 2531
    l = [0 for i in range(s+1)]
    l[0] = ceil(seed)
    for i in range(1, s+1):
        l[i] = (a*l[i-1]+c) % m
    return l[1:s+1]


def second_alg(seed, s):  # fibonacci
    l = [0 for i in range(s+1)]
    for i in range(1, 8):
        l[i] = ceil(i*seed) % m
    for i in range(8, s+1):
        l[i] = (l[i-6]+l[i-3])**3 % m
    return l[1:s+1]


def mean(list):
    return sum(list)/len(list)


def deviation(list, mean_):
    s=0
    for i in range(len(list)):
        s+=((list[i]-mean_)**2)
    return sqrt(s/len(list))


def cv(dev_, mean_):
    return dev_/mean_*100

def rand(s):
    res = []
    for i in range(s):
        res.append(random.randint(1, 10000))
    return res