# filter(fun,seq)

seq = [1,2,3,4,5,6,7,8]

odd = lambda x : True if x%2!=0 else False
filtered_odd_numbers = filter(odd,seq)

# filtered_odd_numbers = filter(lambda x : True if x%2!=0 else False,seq)
print(filtered_odd_numbers)
print(f"Output Odd Numbers : {list(filtered_odd_numbers)}")