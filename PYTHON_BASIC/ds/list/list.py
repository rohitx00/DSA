a = [1,2,3,4,5]

#list methods : 

# append -> append object to the end of the list.
# clear -> remove all items from list.
# copy -> return a shallow copy of the list.
# count -> return number of occurrences of value.
# extend -> extend list by appending elements from the iterable.
# index -> return first index of value.
# insert(index, object) -> insert object befor index.
# pop -> remove and return item at index.
# remove -> remove first occurrence of value.
# reverse -> reverse in place.
# sort -> sort the list in ascendind order and return none.

print("Append")
a.append(6)
print(a)

print("Count")
print(a.count(1))

print("Extend")
a.extend([7,8,9])
print(a)

print("Index")
print(a.index(2))

print("Insert")
a.insert(0,10)
print(a)

print("Reverse")
a.reverse()
print(a)

print("Pop")
print(a.pop())

print("Remove")
a.remove(6)
print(a)

print("Copy")
b = a.copy()
print(b)

print("Sort")
a.sort()
print(a)

print("Clear")
b.clear()
print(b)



