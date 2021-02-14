'''
Python scoping is described by the acronym LEGB:
- Local
- Enclosing
- Global
- Built-in
'''

# print everything in the built-in scope
# import builtins
# print(dir(builtins)) # print everything in the built-in scope

x = 'global x'

def enclosing():
    x = 'enclosing x'

    def inner():
        # nonlocal x            # specify the 'x' you want to use is from the ENCLOSING scope
        # global x              # specify the 'x' you want to use is from the GLOBAL scope
        x = 'inner x'
        print(x)

    inner()
    print(x)


enclosing()
print(x)