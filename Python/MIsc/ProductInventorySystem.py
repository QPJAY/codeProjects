import sqlite3
from employee import Employee

conn = sqlite3.connect('employee.db')

c = conn.cursor()

# c.execute("""CREATE TABLE employees (
#            first text,
#            last text,
#            pay integer
#            )""")

emp_1 = Employee('John', 'Doe', 80000)
emp_2 = Employee('Tom', 'Smith', 100000)



c.execute("INSERT INTO employees VALUES (?, ?, ?)", (emp_1.first, emp_1.last, emp_1.pay))

conn.commit()

c.execute("SELECT * FROM employees")

print(c.fetchall())

conn.commit()

conn.close()