print([]*3)
#output: []
print(('a','b','c')*2)
#output: ('a', 'b', 'c', 'a', 'b', 'c')
print((2)**2)
#output: 4
print([{}]*2)
#output: [{}, {}]
print({3:1}*2)
#output: TypeError: unsupported operand type(s) for *: 'dict' and 'int'
print('123'+2)
#output: TypeError: can only concatenate str (not "int") to str
print(['a','b','c'] + 'rf')
#output: TypeError: can only concatenate list (not "str") to list
print((2,4)**2)
#output: TypeError: unsupported operand type(s) for ** or pow(): 'tuple' and 'int'
z = ['P','L',']']
z += 'SE' #work as extend function and string is iterable of individual character
print(z)
#output: ['P', 'L', ']', 'S', 'E']
