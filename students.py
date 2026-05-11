import pandas as pd
df = pd.read_csv("Student.csv")
def addStudent(df):
    
    name = input("Enter the Student\'s name: ")
    while True:
      try:
        Id = int(input("Enter the Student\'s ID: "))
        break
      except ValueError:
        print("Invalid choice. Enter a valid integer.")
    if (df["ID"] == Id).any():
      print("ID already exists")
      return
    dept = input("Enter the Department: ")
    mark = int(input("Enter the Mark: "))

    df.loc[len(df)] = [name,Id,dept,mark]
    df.to_csv("Student.csv", index=False)


def searchStud(df):
  search = int(input("Enter the ID to search: "))
  dd = df[df["ID"] == search]
  if len(dd) < 1:
    print("No such ID found")
  else:
    print(dd)

def delStud(df):
  delId = int(input("Enter ID to delete: "))
  dd = df[df["ID"] != delId]
  if len(dd) == len(df):
    print("No such ID found.")
    return df
  else:
    while True:
      try:
        doYou = int(input("Confirm Deletion(1.Yes/2.No): "))
        if not 1<=doYou<=2:
          raise ValueError
        break
      except ValueError:
        print("Invalid choice. Enter a valid integer.")
    if doYou == 1:
      print("Successfully deleted")
      return dd
    else:
      print("Deletion cancelled.")
      return df  
def updateStud(df):
  uid = int(input("Enter the ID to update: "))
  if len(df[df["ID"] == uid]) < 1:
    print("ID doesn't exist.")
    return
  while True:
    try:
      toUp = int(input("Enter the component you want to update(1.Name/2.Department/3.Mark): "))
      if not 1<=toUp<=3:
        raise ValueError
      break
    except ValueError:
      print("Invalid choice. Enter a valid integer.")
  if toUp == 1:
    name = input("Enter the new Name: ")
    df.loc[df["ID"] == uid, "Name"] = name
  elif toUp == 2:
    dept = input("Enter the new Department: ")
    df.loc[df["ID"] == uid, "Dept"] = dept
  else:
    mark = int(input("Enter the new Mark: "))
    df.loc[df["ID"] == uid, "Marks"] = mark
  df.to_csv("Student.csv", index = False)
  
def findTopper(df):
  df = df.sort_values(by = "Marks", ascending = False)
  print(df.iloc[0])

def findAvg(df):
  avg = df["Marks"].mean()
  print(f"{avg:0.2f}")

def displaySorted(df):
  df = df.sort_values(by = "Marks", ascending = False)
  print(df)

while True:
  choice = int(input("Enter your choice:\n1.Add Student\n2.View All Students\n3.Search Student by ID\n4.Delete Student by ID\n5.Update Student by ID\n6.Find Topper\n7.Find Average\n8.Display Students based on Mark(Highest to Lowest)\n9.Exit\n"))
  if choice == 9:
    break
  elif choice == 1:
    addStudent(df)
  elif choice == 2:
    print(df)
  elif choice == 3:
    searchStud(df)
  elif choice == 4:
    df = delStud(df)
    df.to_csv("Student.csv", index=False)
  elif choice == 5:
    updateStud(df)
  elif choice == 6:
    findTopper(df)
  elif choice == 7:
    findAvg(df)
  elif choice == 8:
    displaySorted(df)
  else:
    print("Invalid Choice.")
