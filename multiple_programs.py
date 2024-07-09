'''import random

rolls = []
for i in range(100000):
    # randint includes the endpoints
    roll = random.randint(1, 6)
    rolls.append(roll)

count = 0
primes = [2, 3, 5]
for roll in rolls:
    if roll in primes:
        count += 1

size_of_rolls = len(rolls)
print(size_of_rolls)'''

'''L = input().split(' ')  # there is a single space between the quotes
for i in range(len(L) - 1):
    if len(L[i]) > len(L[i + 1]):
        L[i], L[i + 1] = L[i + 1], L[i]

count = 0
for i in range(len(L)):
    if len(L[i]) <= len(L[-1]):
        count += 1

print(count)'''

'''number = 7
divisor = 2003

while number % divisor != 0:
    number = number * 10 + 7

number_of_digits = len(str(number))
print(number_of_digits)'''

'''n = int(input())
M = []
for i in range(n):
    row = []
    for num in input().split(','):
        row.append(int(num))
    M.append(row)

some_var = 0
for i in range(n):
    for j in range(n):
        some_var += M[i][j]

print(some_var)'''

L = [90, 47, 8, 18, 10, 7]
S = [L[0]]  # list containing just one element
for i in range(1, len(L)):
    flag = True
    for j in range(len(S)):
        if L[i] < S[j]:
            before_j = S[: j]  # elements in S before index j
            new_j = [L[i]]		# list containing just one element
            after_j = S[j:]  # elements in S starting from index j
            # what is the size of S now?
            S = before_j + new_j + after_j
            # what is the size of S now?
            flag = False
            break
    if flag:
        S.append(L[i])
print(S)
