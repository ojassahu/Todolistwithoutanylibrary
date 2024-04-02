t=[]
c=[]



def add(x):
  t.append(x)
  show()

def done():
  show()
  print("\nWhich task is complete")
  w=int(input("enter its no."))
  w-=1
  if w >len(t):
    print("wrong task no.")
  else:
     c.append(t[w])
     t.remove(t[w])
     show()

def show():
  n = 1
  for i in t:
    print(n,'.',i)
    n+=1
  
def completed():
  n =1
  for f in c:
    print(n,'.',f)
    n+=1

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
    print('enter ok when task are all added')
    while True:
        a=input("\nEnter the task to be added:\n")
        if a=="ok":
          break
        else:
           add(a)
  elif s=="show":
    show()
  elif s=="done":
    done()
  else:
    print("plz enter correct function\n")