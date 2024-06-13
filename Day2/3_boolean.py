# Boolean are immutable data type
# Membership Operation
print(2 in (3, 4, 5))  # False
print(2 in (2, 4, 5))  # True
print(2 not in (2, 4, 5))  # False


# Identity Operation
a = ()
b = ()
print(a is b)  # True
print(a is not b)  # False


# Concept of Truthy and Falsy

# Truthy
# All those datatypes which are non-empy, non-zero including True itself are truthy
a = 12
b = "Hello"
c = [1, 3, -1]
d = ("a", "b", "c")
e = {"name": "Jane"}
f = {1, 2, 3}
g = True
h = 2.2
print(bool(a)) # True
print(bool(b)) # True
print(bool(c)) # True