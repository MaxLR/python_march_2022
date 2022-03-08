
a = 15
b = 19
c = 25

def my_func(num):
    print("Hi from the print statement")
    print(num)
    output = num * 2 - 3
    print(output)
    return output



my_num = my_func(a)
my_func(b)
my_func(c)

print(my_num)