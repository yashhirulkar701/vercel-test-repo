from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory list to store tasks (Resets when the server restarts)
tasks = []

# Home route to display the to-do list
@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

# Route to add a new task
@app.route('/add', methods=['POST'])
def add_task():
    task = request.form.get('task')
    if task:
        tasks.append(task)
    return redirect(url_for('index'))

# Route to delete a task by index
@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect(url_for('index'))

# Route to edit a task
@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    if request.method == 'POST':
        updated_task = request.form.get('task')
        if updated_task:
            tasks[task_id] = updated_task
        return redirect(url_for('index'))
    else:
        task_to_edit = tasks[task_id]
        return render_template('edit.html', task=task_to_edit, task_id=task_id)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
