

def outer_func(msg):
    message = msg

    def inner_func():
        print(message)

    return inner_func


f1 = outer_func('Hi')
f2 = outer_func('Howdy')
print(f1.__name__)
f1()
f2()