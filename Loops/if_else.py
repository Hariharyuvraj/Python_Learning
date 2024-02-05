
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