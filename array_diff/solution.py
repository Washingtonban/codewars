def array_diff(a, b):
    i = len(a)
    while i > 0:
        if a[i - 1] in b:
            a.pop(i - 1)
        i -= 1
    return a