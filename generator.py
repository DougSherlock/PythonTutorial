'''
A generator saves space by calculating each value ONLY WHEN IT IS REQUIRED.
This results in PERFORMANCE advantages for large lists.
'''

# generator as a FUNCTION - uses the 'yield' keyword
def square_numbers(nums):
    for i in nums:
        yield(i**2) # YIELD keyword makes this a generator


print('Generator in FUNCTION:')
my_nums = square_numbers([1,2,3,4,5])
for num in my_nums:
    print(num)


# generator as a COMPREHENSION
print('Generator in COMPREHENSION:')
my_nums = (x**2 for x in [1,2,3,4,5]) # ROUND BRACKETS make this a generator
for num in my_nums:
    print(num)

