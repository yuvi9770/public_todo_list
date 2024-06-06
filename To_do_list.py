import streamlit as st

# Initialize session state if not already done
if 'tasks' not in st.session_state:
    st.session_state['tasks'] = []

# Function to add a task
def add_task():
    task = st.session_state["new_task"]
    if task:
        st.session_state['tasks'].append({"task": task, "completed": False})
        st.session_state["new_task"] = ""

# Function to remove a task
def remove_task(task_index):
    st.session_state['tasks'].pop(task_index)

# Function to mark a task as complete
def mark_as_complete(task_index):
    st.session_state['tasks'][task_index]["completed"] = True

# Function to clear all tasks
def clear_tasks():
    st.session_state['tasks'].clear()

st.title("To-Do List")

# Input for new task
st.text_input("Enter a task", key="new_task")
st.button("Add Task", on_click=add_task)

# Display the tasks
if st.session_state['tasks']:
    for i, task in enumerate(st.session_state['tasks']):
        task_text = task["task"]
        if task["completed"]:
            task_text += " ✔"
        st.write(f"{i + 1}. {task_text}")
        col1, col2, col3 = st.columns([1, 1, 1])
        col1.button("Remove", key=f"remove_{i}", on_click=remove_task, args=(i,))
        if not task["completed"]:
            col2.button("Complete", key=f"complete_{i}", on_click=mark_as_complete, args=(i,))
    st.button("Clear All", on_click=clear_tasks)
else:
    st.write("No tasks yet!")

st.button("Quit", on_click=st.stop)
