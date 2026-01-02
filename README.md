# TaskTrack API

A simple **To-Do task management API** built with **Flask**
Tested locally with **curl**

---

## Features

- **GET/tasks** : Retrieve all tasks
- **POST/tasks** : Create a new task
- **PUT /tasks/<id>** → Update a task (title or completed status)
- **DELETE /tasks/<id>** → Delete a task by ID

---

## Technologies Used

- Python 3.x
- Flask
- JSON for data exchange
- Tested with curl---

---

## Getting Started

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd Task Track
```

### 2. Install dependencies

```bash
pip install flask
```

### 3. Run the API

```bash
python app.py
```

### 4. Test with curl

- Create a task:
```bash
curl -X POST http://127.0.0.1:5000/tasks -H "Content-Type: application/json" -d "{\"title\":\"Learn Flask\"}"
```
- View all tasks:
```bash 
curl http://127.0.0.1:5000/tasks
```
- Update a task:
```bash
curl -X PUT http://127.0.0.1:5000/tasks/1 -H "Content-Type: application/json" -d "{\"completed\":true}"
```
- Delete a task:
```bash
curl -X DELETE http://127.0.0.1:5000/tasks/1
```

---

## Notes
* Tasks are stored **in memory**, so they will rest if the server restarts.
* Each task has:
    *  id : Unique identifier
    * title : Task name
    * completed: True or False

---
## Author

** Uleko Samuel **
Computer Science Student | Backend & Cloud Enthusiasist

**Skills:** Python . Flask . REST APIs . Git . Azure. DevOps







