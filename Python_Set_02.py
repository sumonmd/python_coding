
setA = {1,2,3}
setB = {4,5,6}

print(" Union Set ")
# Using symbolic method
print(setA | setB)
# Using union method
print(setA.union(setB))


print(" Intersection Set")
A = {1,2,3,4}
B = {3,4,5,6}
#Using Symbolic method
print(A & B)
#Using Intersection method
print(A.intersection(B))


print("Set Difference ")
a = {1,2,3,4}
b = {3,4,5,6}
#Using Symbolic method
print("Difference A-B ",a-b)
print("Difference B-A ", b-a)
# Using method difference
print(a.difference(b))
print(b.difference(a))