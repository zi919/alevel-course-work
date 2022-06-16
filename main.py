import sqlite3
conn=sqlite3.connect("database.db")
c = conn.cursor()
#c.execute("""CREATE TABLE USERS(username_field,password_field)""")
def insert_emp(username,password):
    with conn:
        c.execute("INSERT INTO USERS VALUES (?,?)", (username,password))


def check_exsistance(username,password):
    c.execute(f"SELECT * FROM USERS WHERE username_field {username}")
    return c.fetchall()


def update_pay(emp, pay):
    with conn:
        c.execute("""UPDATE employees SET pay = :pay
                    WHERE first = :first AND last = :last""",
                  {'first': emp.first, 'last': emp.last, 'pay': pay})


def remove_emp(emp):
    with conn:
        c.execute("DELETE from employees WHERE first = :first AND last = :last",
                  {'first': emp.first, 'last': emp.last})

check_exsistance(1,2)
conn.close()