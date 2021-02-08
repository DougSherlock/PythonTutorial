def funcPos(a, b):
    print(a, b)

# funcPos(1, 'cat') # pass by position
# funcPos(b='dog', a='2') # pass by name

def funcDef(a='a', b='b'):
    print(a, b)

# funcDef()
# funcDef('z')
# funcDef('y', 'z')

def funcList(*args):
    for a in args:
        print(a)

# funcList(1, 2)
# funcList(1, 2, 3)

def funcKeyword(**kwargs):
    for key, val in kwargs.items():
        print(f'key:{key} val:{str(val)}')

funcKeyword(animal='dog', car='sedan', color='blue', num1=2, num2=10)

