def sum(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b

# This ensures the following code only runs if the script is executed directly.
# It will not run if the file is imported as a module in another script.

if __name__ == "__main__":  
    x = sum(9, 10)
    y = sub(10, 2)
    z = mul(10, 2)

        
    print(x)
    print(y)
    print(z)
