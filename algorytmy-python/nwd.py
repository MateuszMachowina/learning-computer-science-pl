def nwd(a,b):
    while a != b:
        if a < b:
            b -= a
        else:
            a -= b