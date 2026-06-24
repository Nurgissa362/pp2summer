from functools import reduce
nums = [2,3,4]
product = reduce(lambda x,y:x*y,nums)
print("product:",product)