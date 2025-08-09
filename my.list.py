myList = []
myList.append(10)
myList.append(20)
myList.append(30)
myList.append(40)

print(myList)

myList.insert(1,15)

print(myList)

myList2 = [50, 60, 70]
myList.extend(myList2)

print(myList)

del myList[-1]

print(myList)