def write_name(name):
    with open("telefonNum.txt", "w") as file:
     file.write(name)

def read_found(a):
    with open("telefonNum.txt", "r") as file:
     lst = file.readlines()
    for i in lst:
     if a in lst[i]:
      print (lst[i])
     file.write(name)