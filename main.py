import streamlit as st
from PIL import Image


# CONSTANT
FILEPATH = "todos.txt"


# FUNCTIONS
def get_todos(filepath=FILEPATH):
    """Read a text file and return the list of items"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """Write items in the text file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


todos = get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    write_todos(todos)


st.title("To Do App")
st.subheader("This app helps to boost your productivity!")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()


image = Image.open("./images/cats.png")
st.image(image, caption="Cats")


st.text_input(label="What do you need to do?", placeholder="My new task is...", 
                on_change=add_todo, key="new_todo")


