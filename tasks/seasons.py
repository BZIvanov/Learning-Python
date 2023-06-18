# you will be prompted in the terminal for correct answer, if the answer is incorrect it will keep asking until you provide correct answer
user_input = input("How many seasons in the year?")
while user_input != "4":
    print("Incorrect answer")
    user_input = input("How many seasons in the year?")
print("Correct")
