# Monthly Expend Money Manager
# This program is used to manage monthly expenses, allowing users to add, update, view,calculate, and clear expenses.
# It also provides an option to distribute total expenses among room partners.

# def rent():
#      costs={} #empty dic which store all expensess
#      dates=[] #empty list ,store dates
#      total_cost=0  # total cost variable, store total expended cost

#      while True:
#           print("---Monthly Expend Money Manager---🖥️")
#           choice=input("1.Add Expend cost\n2.Change Expended money\n3.View all spanded money\n4.Calculate Total Expenses\n5.Clear all Expenses\n6.Exit\nchoose option:")
#           if choice=='1':
#                  expenses=input("please Enter expenses name:")
#                  cost=float(input(f"Enter {expenses} cost :")) 
#                  date=input("Enter Date :")
#                  costs[expenses]=cost
#                  dates=date
#                  print(f"\nDate:{date}")
#                  print(f"cots of {expenses} is {cost} ")
#           elif choice=='2':
#                 expenses=input("Enter name of Expend, you want to change cost :")
#                 if expenses in costs:
#                         new_cost=float(input(f"Enter new cost of {expenses}:"))
#                         costs[expenses]=new_cost
#                         print(f"New cost of {expenses} is {cost}")
#                 else:
#                       print(F"Invalid :{expenses} is not present")
#                       print("---Try Agian---")
#                       continue
#           elif choice=='3':
#                 print("---All Expended money list---")
#                 for expenses,cost in costs.items() :
#                    print(f"Date:{dates}: {expenses}:{cost}")
#           elif choice=='4':
#                 total_cost=sum(costs.values()) # to calculate the sum of total cost 
#                 print(f"Total Expend money {total_cost}")
                
#                 distribute=input("you want to distribute total cost with room partners:(yes/no):")
#                 if distribute =="yes":
#                       room_partners=int(input("How many person are in your room:"))
#                       per_person=total_cost/room_partners # divid total cost by number of room partners
#                       print(f"For each person ={per_person}")
#                 elif distribute=='no':
#                       print("OK Thanku")
                      
#                 else :
#                    print("Invalid choice")
#           elif choice=='5':
#                 print("----All biles  are cleared successfuly----")
#                 del costs[expenses]
#           elif choice=='6':
#                 print("----End of program----")
#                 break
        
# rent() 




# Other way to manage expenses

# Monthly Expend Money Manager
def rent():
    # Store expenses as list of dictionaries
    costs = []  
    total_cost = 0

    while True:
        print("\n--- Monthly Expend Money Manager --- 🖥️")
        choice = input("1. Add Expend cost\n2. Change Expended money\n3. View all spent money\n4. Calculate Total Expenses\n5. Clear all Expenses\n6. Exit\nChoose option: ")

        if choice == '1':
            expense = input("Please enter expense name: ")
            cost = float(input(f"Enter {expense} cost: "))
            date = input("Enter date (e.g., 2025-06-30): ")
            costs.append({'expense': expense, 'cost': cost, 'date': date})
            print(f"\nDate: {date}")
            print(f"Cost of {expense} is ₹{cost}")

        elif choice == '2':
            name = input("Enter the name of the expense you want to change: ")
            found = False
            for item in costs:
                if item['expense'] == name:
                    new_cost = float(input(f"Enter new cost for {name}: "))
                    item['cost'] = new_cost
                    print(f"New cost of {name} is ₹{new_cost}")
                    found = True
                    break
            if not found:
                print(f"Invalid: {name} is not present.")
                print("--- Try Again ---")

        elif choice == '3':
            print("\n--- All Spent Money List ---")
            if not costs:
                print("No expenses recorded.")
            else:
                for item in costs:
                    print(f"Date: {item['date']} | {item['expense']}: ₹{item['cost']}")

        elif choice == '4':
            total_cost = sum(item['cost'] for item in costs)
            print(f"\nTotal Expenditure: ₹{total_cost}")

            distribute = input("Do you want to split the total cost among roommates? (yes/no): ")
            if distribute.lower() == "yes":
                roommates = int(input("How many roommates? "))
                if roommates > 0:
                    per_person = total_cost / roommates
                    print(f"Each person should pay: ₹{per_person:.2f}")
                else:
                    print("Invalid number of roommates.")
            elif distribute.lower() == "no":
                print("Okay, not splitting the cost.")
            else:
                print("Invalid input.")

        elif choice == '5':
            costs.clear()
            print("---- All expenses cleared successfully ----")

        elif choice == '6':
            print("---- End of program ----")
            break

        else:
            print("Invalid option. Please try again.")

# Run the function
rent()
