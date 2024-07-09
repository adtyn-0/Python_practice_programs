def checkalnum(s):
    if s.isalnum():
        print(True)
    else:
        print(False)


def checkal(s):
    if s.isalpha():
        print(True)
    else:
        print(False)


def checkdigi(s):
    if s.isdigit():
        print(True)
    else:
        print(False)


def checkupper(s):
    if s.isupper():
        print(True)
    else:
        print(False)


def checklower(s):
    if s.islower():
        print(True)
    else:
        print(False)


if __name__ == '__main__':
    s = input()
    checkalnum(s)
    checkal(s)
    checkdigi(s)
    checklower(s)
    checkupper(s)
