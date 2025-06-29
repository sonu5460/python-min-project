def rent():
     costs={} #empty dic which store all expensess
     dates=[] #empty list ,store dates
     total_cost=0  # total cost variable, store total expended cost
     print("---Monthly Expend Money Manager---🖥️")
     expenses=input("please Enter expenses name:")
     cost=float(input(f"Enter {expenses} cost :")) 
     date=input("Enter Date :")
     costs[expenses]=cost
     dates=date
     print(f"\ndate:{date}")
     print(f"cots of {expenses} is {cost} ")
     while True:
          print("---Monthly Expend Money Manager---🖥️")
          choice=input("choose option:\n1.Add Expend cost\n2.Change Expended money\n3.View all spanded money\n4.Calculate Total Expenses\n5.Clear all Expenses\n6.Exit\n")
          if choice=='1':
                 expenses=input("please Enter expenses name:")
                 cost=float(input(f"Enter {expenses} cost :")) 
                 date=input("Enter Date :")
                 costs[expenses]=cost
                 dates=date
                 print(f"\nDate:{date}")
                 print(f"cots of {expenses} is {cost} ")
          elif choice=='2':
                expenses=input("Enter name of Expend, you want to change cost :")
                if expenses in costs:
                        cost=float(input(f"Enter new cost of {expenses}:"))
                        print(f"New cost of {expenses} is {cost}")
                else:
                      print(F"Invalid :{expenses} is not present")
                      print("---Try Agian---")
                      break
          elif choice=='3':
                print("---All Expended money list---")
                for expenses,cost in costs.items():
                      print(f"{expenses}:{cost}")
          elif choice=='4':
                total_cost=sum(costs.values()) # to calculate the sum of total cost 
                print(f"Total Expend money {total_cost}")
                
                distribute=input("you want to distribute total cost with room partners:(yes/no):")
                if distribute =="yes":
                      room_partners=int(input("How many person are in your room:"))
                      per_person=total_cost/room_partners # divid total cost by number of room partners
                      print(f"For each person ={per_person}")
                elif distribute=='no':
                      print("OK Thanku")
                      break
                else :
                   print("Invalid choice")
          elif choice=='5':
                print("----All biles  are cleared successfuly----")
                del costs[expenses]
          elif choice=='6':
                print("----End of program----")
                break
        
rent()