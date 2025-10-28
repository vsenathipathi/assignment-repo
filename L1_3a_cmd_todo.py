# Simple command line to-do list app that saves tasks to a file.
# Venkat

# view,add, deleete, mark as done, edit,save,

import os,sys,json

# [{"task": "Buy groceries", "done": false}]

filename="todo.json"

print("Welcome to the To-Do List App!")
while True:

    command=input("""\nr -> Read, a -> Add Task, m -> Mark as Done, d -> Delete a Task, q --> Quit the App\nEnter the command: """)
    if command.lower()=="q":
        print("Thank you for using the To-Do List App!")
        break

    def read_and_display_json(filename):
        if os.path.exists(filename):
            with open(filename, "r") as file:
                try:
                    tasks=json.load(file)
                    if len(tasks)==0:
                        print("No tasks present")
                    for id, dic in enumerate(tasks):
                        status="Pending"
                        if dic['done']==True:
                            status="Done"
                        print(f"{id+1}) {dic['task']} - {status}")
                except:
                    print("Unable to Open the Json file.")
        else:
            print("No tasks present")

    if command.lower()=="r":
        read_and_display_json(filename)


    if command.lower()=="a":
        tasks_new=[]
        while True:
            task=input("(Press 'q' to exit) Enter your task : ")
            if task=="q":
                break
            elif task=="":
                continue
            tasks_new.append({"task":task,"done":False})
            # print(tasks_new)
            # print(type(tasks_new))
        
        print('Thank you!.. Trying to add the tasks to the disk')
        if os.path.exists(filename):
            tasks_in_disk=[]
            with open(filename, "r") as file:
                try:
                    tasks_in_disk=json.load(file) # List of Dict
                    tasks_in_disk.extend(tasks_new)
                    print('Successfully saved the task to disk')
                except:
                    print("Unable to write to Disk")
            with open(filename, "w") as file:
                json.dump(tasks_in_disk, file)
        else:
            print("No JSON file Present")

    if command.lower()=="m":
        if os.path.exists(filename):
            with open(filename, "r") as file:
                try:
                    tasks=json.load(file)
                    for id, dic in enumerate(tasks):
                        status="Pending"
                        if dic['done']==True:
                            status="Done"
                        print(f"{id+1}) {dic['task']} - {status}")
                    ind=int(input("Enter the task ID to mark as done: "))
                    if ind > len(tasks):
                        print("Invalid task id")
                        sys.exit(1)
                    tasks[ind-1]['done']=True
                    print("Task marked as done. Yet to save to Disk..")
                    # print(tasks)
                except:
                    print("Unable to Open the Json file.")
            
            with open(filename, "w") as file:
                json.dump(tasks, file)
                print("Successfully saved the task to disk")
            
        else:
            print("No JSON file Present")

    if command.lower()=="d":
        if os.path.exists(filename):
            with open(filename, "r") as file:
                try:
                    tasks=json.load(file)
                    for id, dic in enumerate(tasks):
                        status="Pending"
                        if dic['done']==True:
                            status="Done"
                        print(f"{id+1}) {dic['task']} - {status}")
                    ind=int(input("Enter the task ID to delete: "))
                    if ind > len(tasks):
                        print("Invalid task id")
                        sys.exit(1)
                    tasks.remove(tasks[ind-1])
                    print("Task marked as delete. Yet to save to Disk..")
                except:
                    print("Unable to Open the Json file.")
            
            with open(filename, "w") as file:
                json.dump(tasks, file)
                print("Successfully deleted the task from list")
            
        else:
            print("No JSON file Present")