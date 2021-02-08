# reference: https://realpython.com/iterate-through-dictionary-python/#a-few-words-on-dictionaries

# filter a dictionary using comprehension
a_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
a_filt = { key: value for key, value in a_dict.items() if value > 2 }
# print(a_filt)



# sum the values in a dictionary
incomes = { 'bob': 1000, 'mary': 2000, 'gene': 500 }
# total_income = sum([val for val in incomes.values()])
total_income = sum(incomes.values())
# print(total_income)

prices = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
def discount(current_price):
    return (current_price[0], round(current_price[1] * 0.95, 2))

new_prices = dict(map(discount, prices.items()))
print(new_prices)
print(prices)
