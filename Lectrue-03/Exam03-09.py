#Example of the identity operator

#Two variables pointing to the same object
a = [1, 2, 3]
b = a

#Two variables pointing to different lists with the same content
c = [1, 2, 3]
d = [1, 2, 3]

#Using the identity operator
print(a is b)  # True, since a and b refer to the same object
print(a is c)  # False, since a and c refer to different objects
print(c is d)  # False, since c and d refer to different objects

#Using the equality operator for comparison
print(a == c)  # True, since the content of a and c are equal
print(c == d)  # True, since the content of c and d are equal