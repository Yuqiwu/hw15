import string

def threshold(p):
    u = [x for x in p if x.isupper()]
    l = [x for x in p if x.islower()]
    n = [x for x in p if x.isdigit()]
    if (len(u) * len(l) * len(n) != 0):
        return True
    else:
        return False

print threshold("hello") # false
print threshold("Hello") # false
print threshold("Hello123") # true

def rating(p):
    point = 0
    special = string.punctuation
    if ( len( [x for x in p if x.isupper() ]) > 0 ):
        point += 2
    if ( len( [x for x in p if x.islower() ]) > 0 ):
        point += 2
    if ( len( [x for x in p if x.isdigit() ]) > 0 ):
        point += 2
    if ( len( [x for x in p if x in special ]) > 0 ):
        point += 2
    length = len(p) / 2
    if (length > 4):
        length = 4
    return point + length

print rating("") # 0
print rating("123") # 3
print rating("abc123") # 7
print rating("abc123!@#") # 10
