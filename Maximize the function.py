import itertools

k, m = map(int, input().split())

main_ar = []
for _ in range(k):
    ar = list(map(int, input().split()))
    main_ar.append(ar[1:])

all_combination = itertools.product(*main_ar)
result = 0
for single_combination in all_combination:
    current_value = sum(x * x for x in single_combination) % m
    result = max(current_value, result)

print(result)


'''Sample Input

3 1000
2 5 4
3 7 8 9 
5 5 7 8 9 10 '''
