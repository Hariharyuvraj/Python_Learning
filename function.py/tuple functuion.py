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


# function : 'sorted'
# by using this 'sorted' function can arrange the given 'tuple' by assending order

t=(1,2,3,5,74,6,7,0)   
l=sorted(t)
print(t)
t1=tuple(l)
print(t1)


#by using this 'sorted' function can arrange the given 'tuple' by dessending order

t=(1,2,3,5,74,75,80,10,10,6,7,0)   
l=sorted(t,reverse=True)
print(t)
t1=tuple(l)
print(t1)


#  Tuple packing : collect the values in tuple
a=1
b=2
c=3
d=4
t=(a,b,c,d)
print(t)