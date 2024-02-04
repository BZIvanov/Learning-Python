import os

if not os.path.exists("test.txt"):
    # x flag will create the file
    # not that the file will be created in the directory where you run the script
    my_file = open("test.txt", "x")
    my_file.close()
