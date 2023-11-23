# Python has many built-in fuctions like print(), input(), len(), etc
# But, we can create our own functions to do a specifyc task

def square(x):
    return x * x

for i in range(10):
    print(f"The square of {i} is {square(i)}!")