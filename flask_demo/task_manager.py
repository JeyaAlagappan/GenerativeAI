from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# ---------------------------
# In-memory storage
# ---------------------------
tasks = []
task_id = 1  # Unique ID for each task

# ---------------------------
# API ENDPOINTS
# ---------------------------

# Get all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

# Get single task by ID
@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    task = next((t for t in tasks if t['id'] == id), None)
    if task:
        return jsonify(task)
    return jsonify({'error': 'Task not found'}), 404

# Create a new task
@app.route('/tasks', methods=['POST'])
def create_task():
    global task_id
    data = request.json
    if not data or 'title' not in data:
        return jsonify({'error': 'Title is required'}), 400
    task = {'id': task_id, 'title': data['title'], 'completed': False}
    tasks.append(task)
    task_id += 1
    return jsonify(task), 201

# Update a task
@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    data = request.json
    task = next((t for t in tasks if t['id'] == id), None)
    if not task:
        return jsonify({'error': 'Task not found'}), 404
    task['title'] = data.get('title', task['title'])
    task['completed'] = data.get('completed', task['completed'])
    return jsonify(task)

# Delete a task
@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    global tasks
    tasks = [t for t in tasks if t['id'] != id]
    return jsonify({'message': 'Task deleted'})

# ---------------------------
# FRONTEND ROUTE
# ---------------------------
@app.route('/')
def home():
    """
    Serve the HTML page for interacting with tasks.
    """
    return render_template('index.html')

# ---------------------------
# RUN THE APP
# ---------------------------
if __name__ == "__main__":
    app.run(debug=True)
