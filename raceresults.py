def race_results():
    m = float(input("Enter your time: "))
    x = float(input("Enter your time: "))
    y = float(input("Enter your time: "))
    z = float(input("Enter your time: "))
    num = sorted([m,x,y,z])
    if m == (num[0]):
        print("You won Gold")
    if m == (num[1]):
        print("You won Silver")
    if m == (num[2]):
        print("You won Bronze")
    if m == (num[3]):
        print("No Medal")
def main():
    race_results()
main()