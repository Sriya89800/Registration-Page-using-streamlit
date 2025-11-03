
import streamlit as st
import re
import sqlite3
def init_db():
     conn =sqlite3.connect("user.db")
     c=conn.cursor()
     c.execute('''CREATE TABLE IF NOT EXISTS USERS(EMAIL TEXT PRIMARY KEY, PASSWORD TEXT)''')
     conn.commit()
     conn.close()
def add_user(email,password):
    conn=sqlite3.connect("user.db")
    c=conn.cursor()
    c.execute("INSERT INTO USERS(EMAIL,PASSWORD)VALUES(?,?)",(email,password))
    conn.commit()
    conn.close()
#check the user exist
def user_exists(email):
    conn =sqlite3.connect("user.db")
    c=conn.cursor()
    c.execute("SELECT * FROM USERS WHERE EMAIL=?",(email,))
    result=c.fetchone()
    conn.close()
    return result is not None
def validate_login(email,password):
     conn= sqlite3.connect("user.db")
     c=conn.cursor()
     c.execute("SELECT*FROM USERS WHERE EMAIL=? AND PASSWORD=?",(email,password))
     result=c.fetchone()
     conn.close()
     return  result is not None
USER_FILE = "users.txt"#
# Email & Password Validators
def is_valid_email(email):
    pattern = r'^[a-za-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'   #regular expression to match or validate a valid email
    return re.match(pattern, email)

def is_valid_password(password):
    pattern = r'^(?=.[a-Za-z])(?=.*\d)[A-Za-z\d@#$%^&+=]{6,}$'
    return re.match(pattern, password)

#Read & Write File Utilities
"""def load_users():
    if not os.path.exists(USER_FILE):
        return{}
    with open(USER_FILE, 'r') as f:    
         lines = f.readlines()
    users = {}     
    for line in lines:
        email, password = line.strip().split(',')
        users[email] = password
    return users 
def save_user(email, password):    
    with open(USER_FILE, 'a') as f:
         f.write(f"{email},{password}\n")"""

#Registration From
def register():
    st.subheader("Register")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password" , type="password")

    if st.button("Register"):
        if user_exists(email):
            st.warning("Email already registered.")
        elif password != confirm_password:
            st.error("passwords do not match.")
        elif len(password) < 6 or not any(char . isdigit() for char in password) or not  any(char . isalpha() for char in password):
            st.error("password must be 6+ characters with letters & digits.")
        else:
            add_user(email, password)
            st.success("Account created successfully!")

# Login Form
def login():
    st.subheader("Login")
    email = st.text_input("Email")
    password = st.text_input("password", type="password")

    if st.button("login"):
        if validate_login(email, password):
            st.success(f"Welcome, {email}!")
        else:
            st.error("Invalid credentails!")

# Main App
def main():
    init_db()   #<-- this creates the DB and table
    st.title("login & Register System with SQLite")
    menu = st.selectbox("Menu",["Login","Register"])
    if menu == "Login":
        login()
    else:
        register()

if __name__ == "__main__":
    main()