n = 1     # Global Variable

def fn():
    # global n
    n = 3   # Local Variable
    print("in",n)

fn()
print("out",n)