import streamlit as st
import functions


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


todos = functions.get_todos()

st.title("Мое приложение задач")
st.subheader("Это мое приложение для задач.")
st.write("Это приложение предназначено для повышения вашей продуктивности.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="", placeholder="Добавить новую задачу...",
              on_change=add_todo, key="new_todo")
