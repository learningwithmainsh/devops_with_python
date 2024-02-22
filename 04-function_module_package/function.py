a = int(input("Please enter first number: "))
b = int(input("Please enter second number: "))

def add(a, b):
    add_result = a + b
    return add_result

def sub(a, b):
    sub_result = a - b
    return sub_result

def mul(a, b):
    mul_result = a * b
    return mul_result

def mod(a, b):
    mod_result = a % b
    return mod_result

print(add(a, b))
print(sub(a, b))
print(mul(a, b))
print(mod(a, b))
