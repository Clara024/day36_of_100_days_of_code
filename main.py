#Enter your firatname and lastname separately
yellow = "\033[33m"
default = "\033[0m"
classList=[]

def printList( ):
  print( )
  for i in classList:
    print(i)
  print( )

while True:
  print (f"{yellow}Class Register{default}")
  first = input("What is your firstname?:").strip( ).capitalize( )
  last = input("What is your lastname?:").strip( ).capitalize( )
  fullname = (f"{first} {last}")
  if fullname not in classList:
    classList.append(fullname)

  printList()