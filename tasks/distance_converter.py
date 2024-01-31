print("Type kilometers as a number and press Enter")
# will get the input from the console as a string
kilometers = input()
# parse the string value from the console to a float number
miles = float(kilometers) / 1.6093
print(f"{kilometers} kilometers equals {round(miles, 2)} miles.")
