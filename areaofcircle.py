n = int(input("Enter a number: "))
def square_num(n):
    a = n**2
    my_result = a
    return my_result

def area_circle(n):
    a = (3.14 * (square_num(n)))
    return a

print(area_circle(n))
