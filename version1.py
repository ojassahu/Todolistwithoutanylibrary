t=[]
c=[]



def add(x):
  t.append(x)
  print(t)

def done():
  print(t)
  print("\nWhich task is complete")
  w=int(input("enter its no."))
  w-=1
  if w >len(t):
    print("wrong task no.")
  else:
     c.append(t[w])
     t.remove(t[w])
     print(t)

def show():
  print(t)
  
def completed():
  print(c)

print("clear screen \n\n\n\n\n\n\n\n\n")
print(""" Stop - to stop \n Completed - to show the completed tasks\n Add - to add task \n show - to show the task incomplete \n done - to tick the task which finished \n ********************************************************************""")




while True:
  print("\nEnter the function to performed ")
  s = input()
  if s=="stop":
    break
  elif s=="completed":
    completed()
  elif s=="add":
    a=input("\nEnter the task to be added:\n")
    add(a)
  elif s=="show":
    show()
  elif s=="done":
    done()
  else:
    print("plz enter correct function\n")