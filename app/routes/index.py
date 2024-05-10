from flask import render_template, redirect, request
from app import app, db
from app.models import Task
from datetime import datetime

# Home Page
@app.route("/", methods=["POST", "GET"])
def index():
    # Add a task
    if request.method == "POST":
        current_task = request.form["content"]
        new_task = Task(content=current_task)
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect("/")
        except Exception as e:
            print(f"ERROR:{e}")
            return f"ERROR:{e}"
    # See all curent tasks
    else:
        tasks = Task.query.order_by(Task.created).all()
        return render_template("index.html", tasks=tasks)

# Delete an Item
@app.route("/delete/<int:id>")
def delete(id:int):
    delete_task = Task.query.get_or_404(id)
    try:
        db.session.delete(delete_task)
        db.session.commit()
        return redirect("/")
    except Exception as e:
        return f"ERROR:{e}"
    
# Edit an item
@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id:int):
    task = Task.query.get_or_404(id)
    if request.method == "POST":
        task.content = request.form['content']
        try:
            db.session.commit()
            return redirect("/")
        except Exception as e:
            return f"ERROR:{e}"
    else:
        return render_template('edit.html', task=task)
