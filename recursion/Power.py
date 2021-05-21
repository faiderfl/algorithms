def power(n,p):
    assert p>=0 and int(p)==p, 'Fail'
    if p==0:
        return 1
    else:
        return n*power(n,p-1)

print(power(5,2)) 