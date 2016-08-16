def main():
    lower = 10
    upper = 150
    number = get_num(lower, upper)
    print(chr(number))

def get_num(lower,upper):
    valid_input = False
    while not valid_input:
        try:
            number = int(input("enter a number ({0}-{1}):".format(lower, upper)))
            if lower <= number <= upper:
                valid_input = True
            else:
                print("Enter a valid number")
        except ValueError:
            print("Please enter a valid integer.")
    return number


main()
