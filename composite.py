def num_divisors(num):
    if num <= 0:
        return 0
    if num == 1:
        return 1
    starter = 1
    for nums in range(starter,num):
        if num % nums == 0:
            starter= starter+1
    return starter


def div_count(n):
    divslist= []
    track = 1
    for ns in range(track, n+1):
        divslist.append(num_divisors(ns))
    return divslist


def is_highly_composite_number(num):
    complist = div_count(num)
    for i in complist:
        if i == max(complist):
            if complist.count(max(complist))==1:
                return True
    return False
