filename = input("Enter the file")
with open(filename,"r") as  file:
    content = file.read()
    print(content)
