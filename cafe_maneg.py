# cafe order management system


# menu = {
#     "pizza": 150,
#     "burger": 50,
#     "coffee":60,
#     "pasta": 100,
#     "coke": 40,
#     "biryani": 160,
#     "saled":40
#  }

# order = {}
# total = 0

# while True:
#     print("\nMenu:\nburger:rs 50\npizza:rs 120\ncoffee:rs 60\npasta:rs 100\nbiryani rs:160\nsaled:rs 40'",)
#     item = input("Enter item to order (or 'exit' to finish): ")
    
#     if item.lower() == 'exit':
#         break
#     elif item in menu:
#         qty = int(input("Enter quantity: "))
#         order[item] = order.get(item, 0) + qty
#         total += menu[item] * qty
#     else:
#         print("Item not available!")

# print("\n🧾 Your Order Summary:")
# for item, qty in order.items():
#     print(f"{item} x {qty} = ₹{menu[item]*qty}")
# print("Total Bill: ₹", total)

collection={ }

def student_data(name,marks):
      collection[name]=marks
      
      print(f"Data added for {name} with marks {marks}")
    
def update_marks(name,marks): 
      
      if name in collection:
          collection[name]
          print(f"Marks updated for {name} to {marks}")
      else: 
          print(f"Name {name} not found")


   
def delete_data(name):
   
    if name in collection:
        del collection[name]
        print(f"Name {name} deleted successfully")
    else:
        print(f"Name {name} not found")
    

def display_data():
     if collection.items():
         print("\n--- Student Grades ---")
         for name, marks in collection.items():
                print(f"Name:{name} Marks:{marks}")  
        
     else:
        print("NO data available")
 
            

  

# def main(name,marks):
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
    # main(name,marks)



