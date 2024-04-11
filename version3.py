
def add(e):
  with open('task.txt','a') as f:
    f.write(e +"\n")
  show()

def done():
  show()
  print("\nWhich task is complete")
  w=int(input("enter its no."))
  with open('task.txt','r') as f:
    tasks=f.readlines()
  with open('completed.txt','a') as f:
    f.write(tasks[w-1])
  tasks.remove(tasks[w-1])
  with open('task.txt','w') as f:
    for i in tasks:
      f.write(i)
  
def show():
  with open('task.txt','r') as f:
    content=f.readlines()
    if content:
      print("To do list")
      n=1
      for i in content:
          print(n,'.',i)
          n+=1
  
def completed():
  with open('completed.txt','r') as f:
    content=f.readlines()
    if content:
      print("Task completed")
      n=1
      for i in content:
        print(n,'.',i)
        n+=1 

def clear():
  r = int(input("Enter which list is to be cleared \n Enter 1. to clear task list \n Enter 2. to clear completed list:\n"))
  if r==1 or r==2:
    if r==1:
      with open('task.txt','w') as f:
        f.write(" ")
    else:
      with open('completed.txt','w') as f:
        f.write(" ")
  else:
    print("Wrong no.")

print(""" \n\n\n\n\n\n\n\n\n Stop - to stop \n Completed - to show the completed tasks\n Add - to add task \n show - to show the task incomplete \n done - to tick the task which finished \n Clear - to clear the whole list \n ********************************************************************""")

while True:
  print("\nEnter the function to performed ")
  s = input()
  s= s.lower()
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
  elif s=="clear":
    clear()
  else:
    print("plz enter correct function\n")