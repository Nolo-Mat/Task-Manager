'''This is the section where I've imported libraries'''
from datetime import datetime


def reg_user():
    '''This block of code is ment to add a new user to the user.txt file and display statistics for the admin by:
        - Making Calculations to display the number of tasks and users.
        - Requesting the input of a new username and new password and password confirmation.
        - Validating the new password and confirmation password.
        - Adding the confimered info to the user.txt file if the username doesnt already exist,
        - And otherwise presenting a relevant message.'''

    while True: 
        if username == "admin":
            admin_menu = input('''\n====Admin Menu====
Select one of the options below: 
                                
st -  Statistics relating to tasks and users.
rg -  Registering a new user.
ex -  Exit
:''').lower()
            if admin_menu == "st":
                
                with open("user.txt", "r", encoding='utf-8') as user_Names:
                    num_list = [] 
                    for line in user_Names:
                        num_list.append(line[0])
                        
                    print(f"\nTotal number of users: {len(num_list)}")
                
                with open("tasks.txt", "r", encoding='utf-8') as task_info:
                    num_list2 = []
                    for line in task_info:
                        num_list2.append(line[0])
                        
                    print(f"Total number of tasks: {len(num_list2)}")

            elif admin_menu == "rg":
                while True:
                
                    new_user = input("Enter the new username you want to register: ")
                    new_password = input("Enter a new password: ")
                    confirmation = input("Confirm the afore mentioned password: ")
                    if confirmation == new_password:
                        with open("user.txt", "a", encoding='utf-8') as user_Names:
                            if new_user not in user_name_list:
                            
                                user_Names.write(f'''\n{new_user}, {new_password}''')
                                print("\nA new user has been registered successfully.")
                                break
                            
                            else:
                                print("\nUsername already exists. Please enter a different username and try again.\n")
                    else:
                        print("\nInvalid entry. Password not confirmed. Please try again.")
            elif admin_menu == "ex":
                break
        else:
            print("\nAccess Denied!! ONLY the admin can register a new user!")
            break

       
def add_task():
        '''This block code will allow a user to add a new task to task.txt file by:
                - Requesting the username of the person whom the task is assigned to,
                - The title of a task, the description of the task and the due date of the task.
                - Then I fetch the current date and add the data to the file task.txt'''
        
        username = input("Enter the username of the person to whom the task is assigned: ")
        task_title = input("Enter the title of the task: ")
        task_desc = input("Enter a brief description of the task: ")
        
        Today = date.today()
        str_today = Today.strftime("%d %b %Y")
        
        due_date = input("Enter the due date of the task(day month year): ")
        completion = "No"
        
        with open("tasks.txt", "a", encoding='utf-8') as task_info:
            task_info.write(f"\n{username}, {task_title}, {task_desc}, {str_today}, {due_date }, {completion}")


def view_all():
        '''This block of code will read all the tasks from task.txt file and
         print them to the console in a user friendly manner by:
            - Reading a line from the file using a for loop and splitting that line.
            - Then print the results in a particular format.'''
        
        with open("tasks.txt", "r", encoding='utf-8') as task_info:
            idx = 1
            for line in task_info:
                f = line.split(", ")
                task_num_dict[idx] = f
                print(f'''\n===Task {idx}===
                      Task:              {f[1]}
                      Assigned to:       {f[0]}
                      Date assigned:     {f[3]}
                      Due date:          {f[4]}
                      Task Complete?     {f[5]}
                      Task description:
                        {f[2]}''')
                idx += 1
        
        
def view_mine():
        '''This block of code is opening the tasks.txt file and reading the contents. It is then splitting
        the contents of the file by the comma and assigning the contents to a dictionary. The
        dictionary is then printed out in a formatted way.'''
        
        with open("tasks.txt", "r", encoding='utf-8') as task_info:
            with open("user.txt", "r", encoding='utf-8') as user_info:
                
                idx = 1
                for line in task_info:
                    y = line.split(", ")
                    task_num_dict[idx] = y
                    idx += 1
                
                print(task_num_dict)
                
                for i in task_num_dict.keys():
                    if task_num_dict[i][0] == username:
                        print(f'''\n===Task {i} ===
                        Task:              {task_num_dict[i][1]}
                        Assigned to:       {task_num_dict[i][0]}
                        Date assigned:     {task_num_dict[i][3]}
                        Due date:          {task_num_dict[i][4]}
                        Task Complete?     {task_num_dict[i][5]}
                        Task description:
                            {task_num_dict[i][2]}''')
                            
        # The code below is allowing the user to edit a task. The user can either mark the
        # task as complete or edit the task. If the user chooses to edit the task, they can
        # change the username assigned to the task or the due date of the task.
                counter = 0
                while True:
                    new_taskNum = int(input("\nEnter the number of the task you wish to edit or -1 to exit: "))
                    
                    if new_taskNum == -1:
                        if counter > 0 :
                            print(f'''\n===Task {taskNum} ===
                                Task:              {task_num_dict[taskNum][1]}
                                Assigned to:       {task_num_dict[taskNum][0]}
                                Date assigned:     {task_num_dict[taskNum][3]}
                                Due date:          {task_num_dict[taskNum][4]}
                                Task Complete?     {task_num_dict[taskNum][5]}
                                Task description:
                                    {task_num_dict[taskNum][2]}''')
                            break
                        else:
                            break 
                    else:
                        taskNum = new_taskNum
                        
                        execution = input("""\n===Select one of the options below===
mt  - mark the task as complete
et  - edit the task (eg. change username or due date)
: """)
                        
                        if execution == "mt":
                            if task_num_dict[taskNum][5].strip("\n") == "No": 
                                task_num_dict[taskNum][5] = "Yes\n"
                                counter += 1
                                
                                with open("tasks.txt", "w") as task_info:
                                    for i in task_num_dict:
                                        name = ", ".join(task_num_dict[i])
                                        task_info.write(name) 
                                print(f"Task {taskNum} has been marked complete.")
                            
                            else:
                                print("Task has already been completed.")
                            
                        elif execution == "et":
                            if task_num_dict[taskNum][5].strip("\n") != "Yes":
                                options = input("""\n===Select one of the options below===
un  - to change the username assigned to the task
dd  - to change the due date of the task
: """)
                        
                                if options == "un":
                                    newUser = input("Enter the new username you want to assign to your chosen task: ")
                                    if newUser in user_name_list:
                                        task_num_dict[taskNum][0] = newUser

                                        with open("tasks.txt", "w") as task_info:
                                            for i in task_num_dict:
                                                name = ", ".join(task_num_dict[i])
                                                task_info.write(name)
                                            print(f"The username for task {taskNum} has been changed {newUser}.")
                                                
                                    else: 
                                        print("\nThe entered username is not registered in the system. Please enter a registered username.\n")

                                if options == "dd":
                                    newDueDate = input("""\nEnter the new due date for the task in the following format:
(eg. 22 Oct 2022)
: """)
                                    print(f"The due date for task {taskNum} has been changed from {task_num_dict[taskNum][4]} to {newDueDate}")
                                    task_num_dict[taskNum][4] = newDueDate
                                    
                                    with open("tasks.txt", "w") as task_info:
                                            for i in task_num_dict:
                                                name = ", ".join(task_num_dict[i])
                                                task_info.write(name)
                                                
                            else:
                                print("\nUnable to edit task. The task has already been completed.")

                        else:
                            print("You have made a wrong choice, Please Try again")
                    
                    
def reports():
    ''' This function counts the number of tasks, the number of completed tasks, the number of incomplete tasks,
        the number of overdue tasks, and the percentage of incomplete and overdue tasks.'''
    
#==========================For task_overview.txt =======================================================
    
    with open("tasks.txt", "r", encoding='utf-8') as task_info:
            with open("task_overview.txt", "w") as to:
                
                # The code below is counting the number of tasks that are in the tasks.txt file.
                idx = 1
                for line in task_info:
                    y = line.split(", ")
                    task_num_dict[idx] = y
                    idx += 1
                to.write(f"The total number of tasks is: {len(task_num_dict)}")
                
                # The code below is counting the number of tasks that have been completed.
                com_count = 0
                for i in task_num_dict:
                    if task_num_dict[i][5] == "Yes":
                        com_count += 1       
                to.write(f"\nThe total number of tasks completed is: {com_count}")
                
                # Counting the number of incomplete tasks.
                uncom_count = 0
                for i in task_num_dict:
                    if task_num_dict[i][5] != "Yes":
                        uncom_count += 1
                to.write(f"\nThe total number of incomplete tasks is: {uncom_count}")

                # The code below is counting the number of tasks that are overdue.
                Today = datetime.today()
                formatter_string = "%d %b %Y"

                overdue_count = 0
                for i in task_num_dict:
                    due_date = datetime.strptime(task_num_dict[i][4], formatter_string)
                    
                    if due_date < Today:
                        overdue_count += 1
                        
                to.write(f"\nThe total number of incomplete tasks that are overdue is: {overdue_count}")
            
                # The code below is calculating the percentage of tasks that are incomplete and overdue.
                percent_incom = (uncom_count / len(task_num_dict)) * 100
                
                percent_overdue = (overdue_count / len(task_num_dict)) * 100
                
                to.write(f"\nThe percentage of tasks that are incomplete is: {percent_incom}%")
                to.write(f"\nThe percentage of tasks that are overdue is: {round(percent_overdue)}%")
        
#==========================For user_overview.txt =======================================================

            with open("user_overview.txt", "w", encoding='utf-8') as uo:
                uo.write(f"The total number of users registered is: {len(user_name_list)}")
                uo.write(f"\nThe total number of tasks is: {len(task_num_dict)}")
                
                # The code below  is creating a dictionary of the number of tasks assigned to each user.
                assignment_dict = {}
                for current_user in user_name_list:
                    ta_count = 0
                    for j in task_num_dict:
                        if task_num_dict[j][0] == current_user:
                            ta_count += 1
                            assignment_dict[current_user] = ta_count    
                        else:
                            pass
                        
                uo.write(f"""\nThe total number of tasks assigned to {user_name_list[0]} is: {assignment_dict[user_name_list[0]]}
The total number of tasks assigned to {user_name_list[1]} is: {assignment_dict[user_name_list[1]]}
The total number of tasks assigned to {user_name_list[2]} is: {assignment_dict[user_name_list[2]]}""")
            
                # The code below is calculating the percentage of tasks assigned to each user.
                for i in user_name_list:
                    percent = (assignment_dict[i] / len(task_num_dict)) * 100
                    uo.write(f"\nThe percentage of tasks assigned to {i} is: {percent}%")
                    
                # The code below is calculating the percentage of tasks assigned to each user that are
                # complete, incomplete and overdue.
                new_percent = 100 
                incom_task = {x[0]:0 for x in task_num_dict.values()}
                com_task = {x[0]:0 for x in task_num_dict.values()}

                for i in task_num_dict.values():
                    if i[0] in user_name_list:
                        
                        if i[5].strip("\n") == "No":
                            incom_task[i[0]] +=1
                        else:
                            com_task[i[0]] +=1
                
                for user_val, com_num in com_task.items():
                    num_task = assignment_dict[user_val]
                    new_percent = (com_num / num_task) * 100      
                    uo.write(f"\nThe percentage of tasks assigned to {user_val} that are complete is: {new_percent}%")
                
                for user_val, incom_num in incom_task.items():
                    num_task = assignment_dict[user_val]
                    new_percent = (incom_num / num_task) * 100      
                    uo.write(f"\nThe percentage of tasks assigned to {user_val} that are incomplete is: {new_percent}%")
                
                for user_val, incom_num in incom_task.items():
                    num_task = assignment_dict[user_val]
                    overdue_count = 0
                    for i in task_num_dict:
                        due_date = datetime.strptime(task_num_dict[i][4], formatter_string)
                        if task_num_dict[i][0]==user_val:
                            if due_date < Today and task_num_dict[i][5].strip("\n") == "No":
                                overdue_count += 1
                    new_percent = (overdue_count / num_task) * 100  
                    uo.write(f"\nThe percentage of tasks assigned to {user_val} that are incomplete and overdue is: {new_percent}%")

                print("\nThe reports have been generated successfully.")


def stats():
    """
    The function opens the two files created by the reports() function, and prints the contents of each file
    """

    reports()
    with open("task_overview.txt", "r") as to:
        for line in to:
            print(f"{line}\n")
        
    with open("user_overview.txt", "r", encoding='utf-8') as uo:
        for line in uo:
            print(f"{line}\n")
                

#====Login Section====
# This block of code will allow a user to login.
#     - The code reads usernames and password from the user.txt file
#     - They're stored in a list for usernames and passwords from the file.
#     - And I've used a while loop to validate the user name and password.

password_list = []
user_name_list = []
task_num_dict = {}
with open("user.txt", "r", encoding='utf-8') as user_Names:
    for line in user_Names:
        user, password = line.split(", ")
        
        user_name_list.append(user)
        password_list.append(password.replace("\n", ""))

username = None
while True:
    username = input("Enter your username: ")
    Password = input("Enter your password: ")
    
    if username in user_name_list:
        idx = int(user_name_list.index(username))
        
        if Password == password_list[idx]:
            break
        else:
            print("Invalid password. Please enter the corresponding password.\n")
        
    else:
        print("Invalid entry. Username doesn't exist.\n")
   
while True:
    
    # Presenting the menu to the admin user and making sure that the user input is converted to lower case.
    if username == "admin":
        menu = input('''\nSelect one of the following Options below:
r - Registering a user and admin options
a - Adding a task
va - View all tasks
vm - view my task
gr - generate reports
ds - display statistics
e - Exit
: ''').lower()

        # Conditionals that execute the function that corresponds with the users choice.
        if menu == 'r':
            reg_user()

        elif menu == 'a':
            add_task()

        elif menu == 'va':
            view_all()

        elif menu == 'vm':
            view_mine()
            
        elif menu == 'gr':
            reports()
            
        elif menu == 'ds':
            stats()
        
    # This block of code is ment to exit the program if the user is done using it.   
        elif menu == 'e':
            print('Goodbye!!!')
            exit()

    # An error message for if the user's entry is invalid.
        else:
            print("You have made a wrong choice, Please Try again") 
        
    else:
        menu = input('''\nSelect one of the following Options below:
r - Registering a user and admin options
a - Adding a task
va - View all tasks
vm - view my task
e - Exit
: ''').lower()

        if menu == 'r':
            reg_user()

        elif menu == 'a':
            add_task()

        elif menu == 'va':
            view_all()

        elif menu == 'vm':
            view_mine()
    
        elif menu == 'e':
            print('Goodbye!!!')
            exit()

        else:
            print("You have made a wrong choice, Please Try again")
