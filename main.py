import sqlite3
conn=sqlite3.connect("database.db")
c = conn.cursor()
#c.execute("""CREATE TABLE USERS(username_field,password_field)""")
def insert_emp(username,password):
    with conn:
        c.execute("INSERT INTO USERS VALUES (?,?)", (username,password))
def check_repeadted_username(username):
    c.execute(f"SELECT * FROM USERS WHERE username_field= {username}")
    if c.fetchall()==True:
        return True
    else:
         return False

def check_exsistance(username,password):

    c.execute(f"SELECT * FROM USERS WHERE username_field= {username} and password_field={password}  ")
    return c.fetchall()


def update_password(username, password):
    with conn:
        c.execute(f"UPDATE USERS SET password_field ={password} WHERE  username_field={username}")


def remove_record(username):
    with conn:
        c.execute(f"DELETE from USERS WHERE username_field={username}")


