# While loop can be used for print the condition
# It work like a 'for loop'

prob:1

i=1
while i<=10:
    print('hello yuvraj,welcome to python')
    i=i+1

prob:2
i=1
while i<=12:
    print(i)
    i=i+1

# To print the number from 0 to 20 which is divisible by 3
i=1
while i<=20:
    if i%3==0:
     print(i)
    i=i+1

# To print the number which is divisible by 2 from 0 to 100
i=1
while i<=100:
    if i%2==0:
       print(i)
    i=i+1
    
 # the sum of n number:
    
n=int(input('enter the number:'))
sum=0
i=1
while i<=10:
   sum=sum+i
   i=i+1
print('the sum:',sum)
