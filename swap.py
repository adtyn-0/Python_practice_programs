def swap(s):
    x = ''
    for i in s:
        if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            x += i.lower()
        elif i in "abcdefghijklmnopqrstuvwxyz":
            x += i.upper()
        else:
            x += i
    return x


s = input()
result = swap(s)
print(result)
