def added_functionality(fn):
    def wrapper():
        print("Before")
        fn()
        print("After")

    return wrapper


@added_functionality
def main_functionality():
    print("Main")


main_functionality()
