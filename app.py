from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = []
task_id = 1

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "TaskTrack API is running"
    })


@app.route("/tasks", methods=["POST"])
def create_task():
    global task_id

    data = request.get_json()

    if not data or "title" not in data:
        return jsonify({"error": "Task title is required"}),400

    task = {
        "id": task_id,
        "title": data["title"],
        "completed" :False
    }

    tasks.append(task)
    task_id += 1

    return jsonify(task), 201

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks), 200

@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):

    data = request.get_json()

    for task in tasks:
        if task["id"] == task_id:

            if "title" in data:
                task["title"] = data["title"]

            if "completed" in data:
                task["completed"] = data["completed"]
            return jsonify(task), 200

    return jsonify({"error":"Task not found"}), 404

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):

    global tasks

    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return jsonify({"message":"Task deleted"}), 200


if __name__ == "__main__":
     app.run(host="0.0.0.0", port=5000 )