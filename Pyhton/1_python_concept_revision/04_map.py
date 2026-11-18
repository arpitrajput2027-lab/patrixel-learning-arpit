# map(fun,seq)
seq = [1,2,3,4,5,6,7,8]

odd = lambda x : True if x%2!=0 else False
map_odd_numbers = filter(lambda x : True if x%2!=0 else False,seq)
print(map_odd_numbers)
print(f"Output Odd Numbers : {list(map_odd_numbers)}\n\n\n\n\n\n")
# Output Odd Numbers : [True, False, True, False]


# also used to apply the opration on each element of the Sequence
sqr_nums = map(lambda x : x**2,seq)
print(sqr_nums)
print(f"Output Odd Numbers : {list(sqr_nums)}")
# Output Odd Numbers : [1, 4, 9, 16, 25, 36, 49, 64]