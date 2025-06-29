# Task Manager Program
# This program allows users to add, update, delete, and view tasks with their associated times.
# It uses a dictionary to store tasks and their times, providing a simple command-line interface for task management.

def task():
    tasks={}
    task_no=int(input("how many task you want to add:"))
    for i in range(1,task_no+1):
        task_name=input(f"Enter task {i}:")
        # tasks.append(task_name)
        time=input(f"Enter time for {task_name}:")
        tasks[task_name]=time
        print(f"-your task {task_name} & timing {time} is added successfully-")
    print(f"---Today's tasks---\n{tasks}")
    
    while True:      #program runs until true
        choice=input("Enter a choice:\n1.add\n2.Update\n3.Delete\n4.Time Change\n5.View\n6.Exit\n")
        if choice=='1':
            task_name=input("Enter task: ")
            time=input(f"Enter time for {task_name}:")
            tasks[task_name]=time
            print(f"{task_name} & {time} is successfully added in your task")
        elif choice=='2':
            up_task=input("Enter task name you want to update:")
            if up_task in tasks:
                new_task=input("Enter new task:")
                time=input(f"Enter time for {new_task}:")
                
                # tasks.update({up_task:time,new_task:time})
                del tasks[up_task]
                tasks[new_task]=time
                print(f" task {up_task} is updated to {new_task} ")
                
        elif choice=='3':
            del_task=input("Enter task name you want to delete :")
            if del_task  in tasks:
               del tasks[del_task]
            
               print(f"{del_task} is deleted from task ")
        elif choice=='4':
            task_name=input("Enter task, you  want to change time")   
            if task_name in tasks:
                new_time=input(f"Enter new Time for {task_name}:")
                tasks[task_name]=new_time   
        elif choice=='5':
            print("Today's Task list:\n")
            for task_name, time in tasks.items(): # iterate index 0 to total task indices 
                 print(f"{task_name}:{time}")   # print one by one task
           
        elif choice=='6':
            print("---program is terminated---")
            break
        else:
            print("Invalid choice")
            
task()