list1 = [2, 3, 1, 7, 9]
list2 = [9, 8, 6, 2]

sort1 = sorted(list1)
sort2 = sorted(list2)

totalParts = 0
temp = 0

for i in range(len(sort1)):
    if temp + sort1[i] <= sort2[-1]:
        temp += sort1[i]
        if temp == sort2[-1]:
            temp = 0
            totalParts += 1
            sort2.pop()
    elif temp + sort1[i] >= sort2[-1]:
        temp = 0
        totalParts += 1
        sort2.pop()

totalParts += 1

print(totalParts)
