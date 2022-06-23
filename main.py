import sqlite3
import hashFunctions
conn=sqlite3.connect("database.db")
c = conn.cursor()
#c.execute("""CREATE TABLE USERS(username_field,password_field)""")
def insert(username,password):
    username=hashFunctions.md5(username)
    with conn:
        c.execute("INSERT INTO USERS VALUES (?,?)", (username,password))
def check_repeated_username(username):
    c.execute("SELECT * FROM USERS WHERE username_field=?",(username,))
    if len(c.fetchall())>0:
        return True
    else:
        return False 

def check_exsistance(username,password):
    username=hashFunctions.md5(username)

    c.execute(f"SELECT * FROM USERS WHERE username_field= ? and password_field=? ",(username,password,))
    return c.fetchall()


def update_password(username, password):
    with conn:
        c.execute(f"UPDATE USERS SET password_field ={password} WHERE  username_field={username}")


def remove_record(username):
    with conn:
        c.execute(f"DELETE from USERS WHERE username_field={username}")



