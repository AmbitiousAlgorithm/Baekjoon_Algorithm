res =[]
su =0 

for _ in range(5):
    res.append(int(input()))

for x in res:
    if x >= 40:
        su += x
    else:
        su += 40
print(int(su/5))       