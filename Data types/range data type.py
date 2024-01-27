r=range(100)   #range-0 to 99
print(type(r))
print(r)

for x in r:
     print(x)

r=range(15)    # range-0 to 14
for x in r:
     print(x)

# form-1: range(n)
# from (0 to n-1)
     r=range(10) #:0 to 9
     r1=range(100) #: 0 to 99

# form-2:
# range(begin,end)
# (begin to end-1)
     
r1=range(1,10)      # range-1 to 9
for x in r1:
     print(x)

r2=range(2,50)      # range-2 to 94
for x in r2:
     print(x)

# form-3
# range(begin,end,incresing/decresing)
     
r=range(1,10,1)            # incresing by 1
for x in r:
     print(x)

r1=range(2,50,2)           # incresing by 2
for x in r1:
     print(x)

r2=range(2,100,5)           # incresing by 5
for x in r2:
     print(x)

# similarly range in decresring form decresing by that mentioned value
     
r3=range(50,2,-2)
for x in r3:
     print(x)

r4=range(100,20,-5)
for x in r4:
     print(x)