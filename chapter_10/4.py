def chop(t):
    del t[-1]  # сначала последний
    del t[0]   # потом первый
    return   #  просто return тк в задаче просят вернуть none

print(chop([1, 2, 3, 4]))