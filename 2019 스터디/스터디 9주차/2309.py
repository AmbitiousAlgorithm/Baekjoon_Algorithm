
nine = []
a=0
b =0
for _ in range(9):
    nine.append(int(input()))
weight = sum(nine)

nine.sort()

for i in range(9):
    for j in range(i+1,9):
        if weight - (nine[i] + nine[j]) == 100:
            if i != j:
                a =i #15
                b =j #25임
        else:
            continue 

del nine[a]
del nine[b-1]
print(*nine,sep='\n')