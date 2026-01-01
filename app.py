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


if __name__ == "__main__":
     app.run(debug=True, )