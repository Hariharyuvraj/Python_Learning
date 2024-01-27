#: in set data type duplicate value are not not allowed,
#: slice operater is not alloweded.
#: Set data type is mutable.

s={10,40,"yuvraj","anuja"}
print(s)
s.add(50)
print(s)

s.remove(40)
print(s)
print(type(s))