## Eval funtion is useful to convert to variable type in to our input based value
# As per our input changed this eval funtion show the data type of input value

x=input('enter the any type of value:')
print(type(x))

# If i run this code then it will print type of value is "str"
# But if i used the "eval"function then automatically shows type of entered value.

x=eval(input('enter the any type of value:'))
print(type(x))

x=eval('10+20+30')
print(x,type(x))


