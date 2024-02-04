# opening a file with with will ensure the file is also properly closed
with open("text-file.txt") as f:
    content = f.read()
    print(content)