from fastapi import FastAPI
import database

app = FastAPI()

@app.get("/tasks")
def show_all_tasks():
    database.c.execute("SELECT * FROM tasks")
    tasks = database.c.fetchall()

    all_tasks = []

    if not tasks:
        return {"Message": "No tasks found."}
    
    for task in tasks:
        task_data = {
            "id": task[0],
            "title": task[1],
            "description": task[2],
            "status": task[3]
        }
        all_tasks.append(task_data)

    return {"Tasks": all_tasks}

@app.get("/tasks/{task_id}")
def show_task(task_id: int):
    database.c.execute("SELECT * FROM tasks WHERE id=?", (task_id,))
    task = database.c.fetchone()

    if not task:
        return {"Message": "Task not found."}

    task_data = {
        "id": task[0],
        "title": task[1],
        "description": task[2],
        "status": task[3]
    }

    return {"Task": task_data}

@app.post("/tasks/create new task")
def create_task(title: str, description: str | None = None):
    database.c.execute("INSERT INTO tasks (title, description) VALUES (?, ?)", (title, description))
    database.con.commit()
    return {"Message": "Task created successfully."}

@app.put("/tasks/update task/{task_id}")
def update_task(task_id: int, title: str | None = None, description: str | None = None, status: str | None = None):
    database.c.execute("SELECT * FROM tasks WHERE id=?", (task_id,))
    task = database.c.fetchone()

    if not task:
        return {"Message": "Task not found."}

    updated_title = title if title is not None else task[1]
    updated_description = description if description is not None else task[2]
    updated_status = status if status is not None else task[3]

    database.c.execute("""
        UPDATE tasks
        SET title=?, description=?, status=?
        WHERE id=?
    """, (updated_title, updated_description, updated_status, task_id))
    database.con.commit()

    return {"Message": "Task updated successfully."}

@app.delete("/tasks/delete task/{task_id}")
def delete_task(task_id: int):
    database.c.execute("SELECT * FROM tasks WHERE id=?", (task_id,))
    task = database.c.fetchone()

    if not task:
        return {"Message": "Task not found."}

    database.c.execute("DELETE FROM tasks WHERE id=?", (task_id,))
    database.con.commit()

    return {"Message": "Task deleted successfully."}