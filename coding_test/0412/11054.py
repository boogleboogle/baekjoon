n = int(input())
s_1 = list(map(int, input().split()))
s_2 = s_1[::-1]
# print(s_1)
# print(s_2)
dp_1 = [0 for _ in range(n)]
dp_2 = dp_1[::]
dp_3 = dp_2[::]


for i in range(n):
    for j in range(i):
        if s_1[i] > s_1[j] and dp_1[i] < dp_1[j]:
            dp_1[i] = dp_1[j]
    dp_1[i] += 1

for i in range(n):
    for j in range(i):
        if s_2[i] > s_2[j] and dp_2[i] < dp_2[j]:
            dp_2[i] = dp_2[j]
    dp_2[i] += 1

dp_2= dp_2[::-1]
for i in range(n):
    dp_3[i] = dp_1[i] + dp_2[i] -1
# print(dp_1)
# print(dp_2)
# print(dp_3)
print(max(dp_3))