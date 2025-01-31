#a.

a=10
b=20
print(a and b) #check both operand truthy and give 2nd operand value 
#output is: 20
print(a or b) #check first operand truthy and not check 2nd operand and give first operand value
#output is: 10

#b.

if False:
    print("it is false")
else:
    print("it is true")
#output is: it is true

#c.

if []:
    print("it is balnk.")
else:
    print("it is something else.")
#output is: it is something else.

#d.

if [[]]:
    print("it is balnk")
else:
    print("it is something else")
#output is: it is blank

#e.

if [False]:
    print("it is blank")
else:
    print("it is something else")
#output is: it is blank

#f.

ans = type(range(1,10))
print(ans)
#output is: <class 'range'>
