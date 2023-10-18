"""PYTHON CASTING
This is the act of specifying a variable type using constructor functions such as;
int(), float() and string()"""

#Example to explain int() Constructor
x = int(2) # variable x will have a value of 2 useable for mathematical applications or operations
y = int(2.854) # variable y will have a value of 2 by constructing the float literal into intinger literal useable for mathematical operations.
z = int("3") # variable z will have a value of 3 by constructing the string literal into intinger literal useable for mathematical operations.
f = x + y + z
print(y)
print(z)
print(f) # the output will be 7

#Example to explain float() constructor
j = float(1) # variable j will have a value of 1.0 by constructing the intinger literal into float literal.
k = float(2.8) # variable k will retain the float literal as it is; 2.8
l = float("3") # varialbe l will have value of 3.0 by constructing the string literal into float literal.

print(j, k, l)
print(j)
print(k)
print(l)

#Example to explain string() constructor
m = str("s1") # variable m will retain the string literal.
n = str(2) # variable n will have value '2' by constructing the intinger literal into string literal.
z = str(3.0) # variable z will have value '3.0' by constructing the float literal into string literal.

print(m)
print(n)
print(z) 