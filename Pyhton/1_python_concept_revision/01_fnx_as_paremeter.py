def add(num):
    return num + 1

def sqr(num):
    return num**2

number = int(input("Enter the Number :"))
# res_1 = add(number)
# res_2 = sqr(res_1)

res = sqr(add(number))
print(f"output is : {res}")