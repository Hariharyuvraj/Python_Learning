# list comprehension:

list=[x for x in range(1,11)]
print(list)

list=[x*x for x in range(1,11)]
print(list)

l=[2*x for x in range(1,11)]
print(l)

l=[3*x for x in range(1,11)]
print(l)

l1=[4*x for x in range(1,11)]
print(l1)

l1=[5*x for x in range(1,11)]
print(l1)

#conversion of 'str' to list:

s="i love you"
l3=s.split()
print(l3)

s='i love you'
l4=s.split()
for x in l4:
    print(x)

s='hello how are you'
s2=s.split()
print(s2)

for x in s2:
    print(x)

s='hello'
for x in range(5):
    print('hello')

s1=s.split()
print(s1)

for x in s:
    print(x)
    
s='i love you anuja'
s1=s.split()
print(s1)
