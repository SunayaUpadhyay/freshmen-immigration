# https://codeforces.com/contest/282/problem/A

n = int(input())
x = 0

statements = [input() for i in range(n)]
for statement in statements:
    if "++" in statement:
        x += 1
    else:
        x -= 1

print(x)
