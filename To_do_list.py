import streamlit as st

# Define an empty list to store tasks
tasks = []

# Function to add a task
def add_task():
    task = st.session_state["new_task"]
    if task:
        tasks.append({"task": task, "completed": False})
        st.session_state["new_task"] = ""
        st.experimental_rerun()

# Function to remove a task
def remove_task(task_index):
    tasks.pop(task_index)
    st.experimental_rerun()

# Function to mark a task as complete
def mark_as_complete(task_index):
    tasks[task_index]["completed"] = True
    st.experimental_rerun()

# Function to clear all tasks
def clear_tasks():
    tasks.clear()
    st.experimental_rerun()

st.title("To-Do List")

# Input for new task
st.text_input("Enter a task", key="new_task")
st.button("Add Task", on_click=add_task)

# Display the tasks
if tasks:
    for i, task in enumerate(tasks):
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
