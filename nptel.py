'''def mystery(l, v):
    if len(l) == 0:
        return (v)
    else:
        return (mystery(l[:-1], l[-1]+v))


mystery([22, 14, 19, 65, 82, 55], 1)'''

'''triples = [(x, y, z) for x in range(2, 4)
           for y in range(2, 5) for z in range(5, 7) if 2*x*y > 3*z]
print(triples)'''


def longest_palindrome_subword(word):
    n = len(word)
    dp = [[0] * n for _ in range(n)]
    max_length = 0
    start = 0

    for i in range(n):
        dp[i][i] = 1
        max_length = 1

    for i in range(n - 1):
        if word[i] == word[i + 1]:
            dp[i][i + 1] = 1
            max_length = 2
            start = i

    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if word[i] == word[j] and dp[i + 1][j - 1]:
                dp[i][j] = 1
                if length > max_length:
                    max_length = length
                    start = i

    return max_length, word[start:start + max_length]


N = int(input())
word = input().strip()

length, subword = longest_palindrome_subword(word)

print(length)
print(subword)
