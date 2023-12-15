lines = []
list2 = []
list3 = []

liist=[]
#1.uzd
with open("data.txt", 'r') as f:
    next(f)
    for line in f:
        list2 = line.strip().split(',')
        if list2[4] == 'Oman':
            liist.append(list2[6])

sortedList = sorted(liist)
print(sortedList[0])
llist=[]


#2.uzd
with open("data.txt", 'r') as f:
    next(f)
    for line in f:
        lines = line.strip().split(',')
        if lines[4] == 'Latvia':
            llist.append(int(lines[8]))
print(sum(llist))


#3.uzd
lisst = []
with open("data.txt", 'r') as f:
    next(f)
    for line in f:
        list3 = line.strip().split(',')
        if list3[4] == 'Latvia' and list3[7] == 'Telecommunications':
            lisst.append(int(list3[8]))

print(sum(lisst))

#4.uzd
listt = []
list4 = []
times = 0
with open("data.txt", 'r') as f:
    next(f)
    for line in f:
        list4 = line.strip().split(',')
        if list4[4] == 'Latvia' and list3[3] == str(list3[3]).startswith("https://"):
            times +1

print(times)

