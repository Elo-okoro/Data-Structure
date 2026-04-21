
A={1,1,1,2,2,2,3,4,5,5}
print(A)
A.add(6)
A.add(10)
A.add(20)
print(A)
B={4,5,6,7,8}
C=A.union(B)
print( C)
D=A.intersection(B)
print(D)
E=A.difference(B)
print(E)
F=A.symmetric_difference(B)
print(F)
