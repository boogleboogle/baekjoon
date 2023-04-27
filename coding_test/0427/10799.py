import sys
input = sys.stdin.readline

s = input().rstrip()
s = s.replace("()","L",-1)

result,stack = 0,0
for i in s:
    if i == "(":
        stack += 1
    elif i == "L":
        result += stack
    else:
        stack -= 1
        result += 1
print(result)