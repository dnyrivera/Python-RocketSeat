# pylint: disable=import-error
from flask import Flask, jsonify, request
from models.task import Task

app = Flask(__name__)

# CRUD - Create, Read, Update, Delete

tasks = []
TASK_ID_CONTROL = 1


@app.route("/tasks", methods=["POST"])
def create_task():
    global TASK_ID_CONTROL  # pylint: disable=global-statement
    data = request.get_json()

    new_task = Task(
        task_id=TASK_ID_CONTROL,
        title=data["title"],
        description=data.get("description", ""),
    )
    TASK_ID_CONTROL += 1
    tasks.append(new_task)
    print(tasks)
    return jsonify({"message": "New Task Created"})


@app.route("/tasks", methods=["GET"])
def get_all_tasks():
    task_list = [task.to_dict() for task in tasks]
    output = {"tasks": task_list, "total_tasks": len(task_list)}
    return jsonify(output)


@app.route("/tasks/<int:task_id>", methods=["GET"])
def get_single_task(task_id):
    task_list = [t for t in tasks if t.task_id == task_id]
    output = (
        {"task": task_list[0].to_dict()} if task_list else {"message": "Task not found"}
    )
    return jsonify(output), (200 if task_list else 404)


@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    task_list = [t for t in tasks if t.task_id == task_id]
    if not task_list:
        return jsonify({"message": "Task not found"}), 404
    return jsonify({"message": "Task Updated"}), 200


# Running this way to Local Development
if __name__ == "__main__":
    app.run(debug=True)
