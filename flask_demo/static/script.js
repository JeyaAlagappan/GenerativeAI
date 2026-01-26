const apiUrl = '/tasks';

// Fetch and display tasks
async function loadTasks() {
    const res = await fetch(apiUrl);
    const tasks = await res.json();
    const list = document.getElementById('taskList');
    list.innerHTML = ''; // Clear existing items

    tasks.forEach(task => {
        const li = document.createElement('li');
        li.textContent = task.title + (task.completed ? ' ✅' : '');
        
        // Complete button
        if (!task.completed) {
            const completeBtn = document.createElement('button');
            completeBtn.textContent = 'Complete';
            completeBtn.onclick = () => updateTask(task.id, {completed: true});
            li.appendChild(completeBtn);
        }

        // Delete button
        const deleteBtn = document.createElement('button');
        deleteBtn.textContent = 'Delete';
        deleteBtn.onclick = () => deleteTask(task.id);
        li.appendChild(deleteBtn);

        list.appendChild(li);
    });
}

// Add new task
async function addTask() {
    const input = document.getElementById('newTask');
    const title = input.value;
    if (!title) return alert("Enter a task title");

    await fetch(apiUrl, {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({title})
    });

    input.value = '';
    loadTasks();
}

// Update task
async function updateTask(id, data) {
    await fetch(`${apiUrl}/${id}`, {
        method: 'PUT',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(data)
    });
    loadTasks();
}

// Delete task
async function deleteTask(id) {
    await fetch(`${apiUrl}/${id}`, {method: 'DELETE'});
    loadTasks();
}

// Load tasks on page load
window.onload = loadTasks;
