def main():
    name = input("what is your name:")
    get_name(name)


def get_name(name):
    while name == "":
        name = input("what is your name:")
    print_string(name, 5)
    print_string(name, 2)


def print_string(name, step):
    for c in name[::step]:
        print(c, end="")
    print()


main()