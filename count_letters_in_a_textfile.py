filename = input("Enter the file")
with open(filename,"r") as  file:
    content = file.read()
    a_count = 0
    y_count = 0
    h_count = 0

    for ch in content:
      if(ch == 'a'):
          a_count+=1
      elif(ch == 'y'):
          y_count +=1
      elif(ch == 'h'):
          h_count+=1
print("a_count:",a_count)
print("y_count:",y_count)
print("h_count:",h_count)
