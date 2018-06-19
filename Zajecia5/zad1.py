width = int(input())
f = open("plik.txt")
count = 0
res = ''
for line in f:
    for char in line:
        count += 1
        res += char
        if count == width:
            print(res)
            count = 0
            res = ''

f.close()
