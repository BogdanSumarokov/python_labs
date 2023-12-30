res = []

# Первый способ 
for i in range(10, 101):
    if str(i) == str(i)[::-1] and str(i ** 3) == str(i ** 3)[::-1]:
        res.append(i)

# Второй способ 
# for i in range(11, 101, 10):
#     if str(i) == str(i)[::-1] and str(i ** 3) == str(i ** 3)[::-1]:
#         res.append(i)

print(res)