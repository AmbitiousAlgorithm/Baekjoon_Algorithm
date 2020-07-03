N = int(input())

for i in range(N):
    word = input()

    for j in range(0,len(word)-1):
        if word[j] != word[j+1]:
            if(word[j] in word[j+1:]):
                N -= 1
                break
print(N)

