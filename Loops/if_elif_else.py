
# prob:01
n=22

if (n % 2) != 0:
    print("werid")      # first condtion
 
# second contion
elif n%2 == 0 and n>2 and n<=5:
        print("Not Weird")

# third condtion
elif n%2 == 0 and n>6 and n<20:
        print("Weird")

# fourth condtion
elif n%2 == 0 and n>=20:
        print(" this is fouth :not Weird")

        #: List is mutable ,we can change init

# prob: 02
        username=input('enter name:')
        password=input ('enter pass:')

        if username =='sagar' and password =='shiv':
               print("valid user")
        else:
               print("not valid user")

# prob:03
               
a=3
b=5
if a>b:
       print('yes')
else:
       print('no')

a=50
b=67
if a<b:
       print("correct")
else:
       print('incorrect')

a=True
b=False
if a>b:
       print('yes')
else:
       print('no')


# prob:04
       
name=input('enter name:')
if name=='yuvraj':
       print('welcome boss,how may i help you')
else:
       print('sorry invalid entry')


# prob:05
## if -elif-else condition:
       
brand=('enter your favourate brand:')
if brand=='beer':
       print('this is child brand')
elif brand=='ro':
       print('this is comman brand')
elif brand=='rs':
       print('this is good')
elif brand=='fo':
       print('this is very good')
else:
       print('other brand are not available')

#prob:06
## to find the biggest number from two number
       
a=int(input('enter the first number:'))
b=int(input('enter the second number:'))
if a>b:
       print('biggest number is',a)
else:
       print('biggest number is',b)

## to find the smallest number from two number
       
a=int(input('enter the first number:'))
b=int(input('enter the second number:'))
if a<b:
       print('smallest number is',a)
else:
       print('smallest number is',b)  

# Prob:07
n=int(input('enter the number from 0 to 5:'))
if n==0:
       print('zero')
elif n==1:
       print('one')
elif n==2:
       print('two')
elif n==3:
       print('three')
if n==4:
       print('four')
else:
       print('enter the number below the 5')


n=input('enter the digit from 0 to 9:')
list=['zero','one','two','three','four','five','six','seven','eight','nine']
print(list[n])




