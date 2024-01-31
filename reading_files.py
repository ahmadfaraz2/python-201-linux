# When using "with" we don't have to worry about closing the file.

with open("greeting.txt", "r") as file:
    print(file.read())


# To access the content of the file outside the "with" indentation

with open("greeting.txt", "r") as file:
    content = file.read()


print("Content of the file is: ", content)        