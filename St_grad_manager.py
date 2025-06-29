# Student Grade Management System

collection={ }
# This function adds student data to the collection
def student_data(name,marks):
      collection[name]=marks
      
      print(f"Data added for {name} with marks {marks}")

# This function updates the marks of a student if the name exists in the collection  
def update_marks(name,marks): 
      
      if name in collection:
          collection[name]
          print(f"Marks updated for {name} to {marks}")
      else: 
          print(f"Name {name} not found")

# This function deletes a student's data from the collection if the name exists
def delete_data(name):
   
    if name in collection:
        del collection[name]
        print(f"Name {name} deleted successfully")
    else:
        print(f"Name {name} not found")
    
# This function displays all student data in the collection
def display_data():
     if collection.items():
         print("\n--- Student Grades ---")
         for name, marks in collection.items():
                print(f"Name:{name} Marks:{marks}")  
        
     else:
        print("NO data available")
 
            

def main(name,marks):
    while True:
        print("\n--- Student Grade Management System ---")
       
        print("1.Add Student Name & Grade\n2.Update Student Grade\n3.Delete student record\n4.Display all student records\n5.exit")
        choice=input("choose an option:")
        if choice=='1':
            name=input("Enter student name:")
            marks=int(input("Enter student marks:"))
            student_data(name,marks)
        elif choice=='2':
            name=input("Enter name to update marks:")
            marks=int(input("Enter new marks:"))
            update_marks(name,marks)
        
        elif choice=='3':
            name=input("Enter name to delete:")
            delete_data(name)
        elif choice=='4':
            display_data()
        elif choice=='5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice! please try again.")
main(name="name",marks="marks")