# Comprehension concept is applicable for 'dict' also 
# By using this concept we can crete the 'dict' easily
 
d={x:x*x for x in range(1,6)}
print(d)

# # In multiple of 3 number can print in 'dict

d1={x:3*x for x in range(1,6)}
print(d1)


# In multiple of 5 number can print in 'dict'
d2={x:5*x for x in range(1,11)}
print(d2)

# sq of 'x' in given range can print in 'dict' 

d3={x:3**x for x in range(1,6)}
print(d3)

d4={x:10*x for x in range(1,11)}
print(d4)