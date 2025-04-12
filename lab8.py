import random
#1
nums = []
min_posit = []
for i in range(random.randint(10, 20)):
    nums.append(random.randint(-1000, 1000))
print(nums)
for num in nums:
    if num > 0:
        min_posit.append(num)
print(min(min_posit))

#2
n, m = int(input()), int(input())
mat = [list(map(int, input().split())) for p in range(n)]
count_neg = 0
i = 0
j = m - 1
while i < n and j >= 0:
    if mat[i][j] < 0:
        count_neg += n - i
        j -= 1
    else:
        i += 1
print(count_neg)

#3
n = int(input())
mat2 = [input().strip() for _ in range(n)]
m = len(mat2[0]) if n > 0 else 0
count2 = 0

for j in range(m):
    is_ordered = True
    for i in range(1, n):
        if mat2[i][j] < mat2[i-1][j]:
            is_ordered = False
            break
    if not is_ordered:
        count2 += 1
print(count2)
