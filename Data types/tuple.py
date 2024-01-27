#: tuple is immutable data type,once we created it may nat be changed

t=(10,20,50,"pooja","anuja")
print(type(t))

print(id(t))

# slice operater we can use in tuple
s1=t[1:2]
print(s1)

s2=t[0:4]
print(s2)

# Note:in tuple single value ends with , then it type tuple
