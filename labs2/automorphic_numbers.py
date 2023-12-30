res = []

for i in range(1,1001):
    if str(i ** 2).endswith(str(i)):
        res.append(i)

print(res)