if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())
        sum = 0
        for i in range(n):
            if (i % 3 == 0) or (i % 5 == 0):
                sum += i
        print(sum)
