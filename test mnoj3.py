n = list(map(int, input().split()))
x = set()
for i in n:
    if i in x:
        print("YES")
    else:
        x.add(i)
        print("NO")
        