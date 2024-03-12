#: tuple is immutable data type,once we created it may nat be changed

t=(10,20,50,"pooja","anuja")
print(type(t))

print(id(t))

# slice operater we can use in tuple
s1=t[1:2]
print(s1)

s2=t[0:4]
print(s2)

# Note:in tuple single value ends with , then it shows type 'tuple'


# function: 'reverse' the 'tuple'
 
t=(1,2,3,4,5,6,7,8,9)
r=reversed(t)
t1=tuple(r)
print(t1)

# function:count()
# by using this function we can count the specific number in the 'tuple'

t=(1,2,3,1,1,1,4,5,6,7,8,9)
print(t.count(1))

# function: len()

t=(2,1,2,3,1,1,1,4,5,6,7,8,9)
print(len(t))

print(t.index(1))      # using this we can find index of specific number in 'tuple'
