def show_menu():
    print("\n===== To-Do list Menu =====")
    print("1. Add task")
    print("2. View Tasks")
    print("3. Delete Tasks")
    print("4. Exit")

def add_task():
    task = input("ENter yout new tassk: ")
    with open("tasks.txt", "a") as file:
        file.write(task +  "\n")
    print(" Task Added Sucessfully")

def view_tasks():
    try:
        with open("tasks.txt", "r") as file:
           tasks = file.readlines()
           if not tasks:
             print(" No tasts yet.") 
           else:
                print("\nYour Tasks:")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task.strip()}")
    except FileNotFoundError:
         print("No Task File Found yet. Please add a task first.")


def delete_task():
    view_tasks()
    try: 
        task_number = int(input("Enter the task number to Delete: "))
        with open("tasks.txt","r") as file:
           tasks = file.readlines()

        if 1  <= task_number <= len(tasks):
            del tasks[task_number - 1] 
            with open("tasks.txt", "w") as file:
                  file.writelines(tasks)
            print("  tasked deleted successfully!")
        else:
            print(" Invalid task number.")
    except ValueError:
       print(" Please enter a valid number.")
   
def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ")
       
        if choice == "1": 
            add_task()
        elif choice == "2": 
            view_tasks()
        elif choice == "3": 
            delete_task()
        elif choice  == "4":
            print(" Exiting....Have a productive day!")
            break
        else:
             print(" Invalid choice. Please select From !-4.")

if __name__ =="__main__":
   main()
