import math
def school_busses():
    x = int(input("Enter number of students: "))
    y = (x/52)
    if y.is_integer():
        print("The number of busses required is " + str(y))
    if not y.is_integer():
        z = math.ceil(y)
        print("The number of busses required is " + str(z))

def main():
    school_busses()

main()