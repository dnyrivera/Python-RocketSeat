import platform
import subprocess
import time
from typing import TypedDict


def clear_console():
    if platform.system() == "Windows":
        subprocess.run(["cmd", "/c", "cls"], check=False)
    else:
        subprocess.run(["clear"], check=False)


class Task(TypedDict):
    name: str
    completed: bool


def add_task(tasks: list[Task], task_name: str) -> None:
    new_task: Task = {"name": task_name, "completed": False}
    tasks.append(new_task)
    print(f"\nTask: {new_task['name']} added successfully!\n")
    time.sleep(2)
    clear_console()


def list_tasks(tasks: list[Task]) -> None:

    print("\n__________List Tasks__________\n")
    for index, task in enumerate(tasks, start=1):
        status = "✓" if task["completed"] else " "  # show the task status only
        print(f"{index}.[{status}] {task['name']}")
    print("\n")


def update_task(tasks: list[Task], task_index: int, task_new_name: str) -> None:
    print("\n__________Update Task__________\n")
    if task_index < 1 or task_index > len(tasks):
        print("Invalid task index")
    else:
        old_task_name = tasks[task_index - 1]["name"]
        tasks[task_index - 1]["name"] = task_new_name
        print(f"Task Name: {old_task_name} updated to -> {tasks[task_index-1]['name']}")


def complete_task(tasks: list[Task], task_index: int) -> None:
    if task_index < 1 or task_index > len(tasks):
        print("Invalid task index")
    else:
        tasks[task_index - 1]["completed"] = True
        print(f"Task {task_index} was completed!\n")


def delete_completed_tasks(tasks: list[Task]):
    tasks[:] = [task for task in tasks if not task["completed"]]
    print("All Completed Tasked have been deleted")


tasks_list: list[Task] = []

while True:
    print("Manager Task Menu")
    print("[1] Add Task")
    print("[2] List Tasks")
    print("[3] Update Task")
    print("[4] Complete Task")
    print("[5] Delete Completed Tasks")
    print("[6] Exit")

    option = input("Choose an option: ")

    if option.strip() == "1":
        clear_console()
        new_name = input("Input the New Task name: ")
        add_task(tasks=tasks_list, task_name=new_name)

    elif option.strip() == "2":
        clear_console()
        list_tasks(tasks=tasks_list)

    elif option.strip() == "3":
        clear_console()
        list_tasks(tasks=tasks_list)
        update_index = int(input("Number of the task to update: "))
        new_task_name = input("Input the new task name: ")
        update_task(tasks_list, update_index, new_task_name)

    elif option.strip() == "4":
        clear_console()
        list_tasks(tasks_list)
        complete_index = int(input("Number of the task to complete: "))
        complete_task(tasks_list, complete_index)

    elif option.strip() == "5":
        clear_console()
        delete_completed_tasks(tasks_list)
        list_tasks(tasks_list)

    elif option.strip() == "6":
        print("Program Finished")
        break
