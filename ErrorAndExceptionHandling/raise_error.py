def print_info(info_text, color):
    colors = ("red", "green", "yellow")

    if type(info_text) is not str:
        raise TypeError("Info text must be a string")
    if type(color) is not str:
        raise TypeError("Color must be a string")
    if color not in colors:
        raise ValueError("Invalid color")

    print(f"Info: {info_text}. Flag: {color}")


print_info("Something went wrong", "dark-red")  # ValueError: Invalid color
