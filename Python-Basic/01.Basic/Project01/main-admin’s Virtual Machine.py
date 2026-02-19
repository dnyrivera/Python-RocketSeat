from typing import Any, Dict, List


def add_task(tasks: list[Dict[str, Any]], task_name: str) -> None:
    new_task: Dict[str, Any] = {
        "name": task_name,
        "completed": False
    }
    tasks.append(new_task)
    print(f"\nTask: {new_task['name']} added successfully!\n")


def list_tasks(tasks: list[Dict[str, Any]]) -> None:
    print("\n__________List Tasks__________\n")
    for index, task in enumerate(tasks, start=1):
        status = "✓" if task["completed"] else " "
        print(f"{index}.[{status}] {task['name']}")
    print("\n")


def update_task(tasks: list[Dict[str, Any]], task_index: int, task_new_name: str) -> None:
    print("\n__________Update Task__________\n")
    if task_index < 1 or task_index > len(tasks):
        print("Invalid task index")
    else:
        old_task_name = tasks[task_index-1]["name"]
        tasks[task_index-1]["name"] = task_new_name
        print(
            f"Task Name: {old_task_name} updated to -> {tasks[task_index-1]['name']}")


def complete_task(tasks: list[Dict[str, Any]]) -> None:
    pass


def delete_completed_tasks():
    print("Delete Completed Tasks")


tasks_list: List[Dict[str, Any]] = []

while True:
    print("Manager Task Menu")
    print("[1] Add Task")
    print("[2] List Tasks")
    print("[3] Update Task")
    print("[4] Complete Task")
    print("[5] Delete Completed Tasks")
    print("[6] Exit")

    option = input("Choose an option: ")

    if option == "1":
        task_name = input("Input the New Task name: ")
        add_task(tasks=tasks_list, task_name=task_name)
    elif option == "2":
        list_tasks(tasks=tasks_list)
    elif option == "3":
        list_tasks(tasks=tasks_list)
        task_index = int(input("Number of the task to update: "))
        new_task_name = input("Input the nem task name: ")
        update_task(tasks_list, task_index, new_task_name)
    elif option == "4":
        list_tasks((tasks_list))
        task_index = int()
        print("Complete Task")
    elif option == "5":
        print("Delete Completed Tasks")
    elif option == "6":
        print("Exit")
        break

print("Program Finished")
