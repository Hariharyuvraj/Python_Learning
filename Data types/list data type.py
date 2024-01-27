l=[10,20,30,'yuvraj','anuja','pune','tushar']
print(l)

#:In list data type we can add any values like int,str,etc.

#: Append() 
#: by using append we can add value in list 
l.append(230)
print(l)
l.append('bunty')
print(l)

# remove: by using this operater we can remove item from the list

l.remove(230)
print(l)

l.remove('bunty')
print(l)

#:if i want to replace the item by another item in list then i can use following

l[1]=1991
print(l)

l[-1]="dada"
print(l)

#: in list we can use slice operater

s1=l[1:3]
print(s1)

s2=l[1:0]
print(s2)

s3=l[1:-1]
print(s3)