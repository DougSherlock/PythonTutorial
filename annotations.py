# annotations are purely informative - they are not enforced
# p1 should be an int
# p2 should be a string
# return value should be a string
def foo(p1: int, p2: str) -> str:
    f'p1:{str(p1)}, p2:{p2}'

res = foo(5, 'cat')
print(type(res))
res = foo('dog', 'cat')
print(type(res))
print(foo.__annotations__)