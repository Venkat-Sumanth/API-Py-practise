import mysql.connector

#STEP:1- Connect to the MYSQL database
try:
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="Venkat@123",
        database="crud_python"
    )
    mycursor=conn.cursor()
    print("Connection Established")
except mysql.connector.Error as err:
    print(f"Connection Error: {err}")
    exit(1)

# STEP:2- Create Database (if it doesn't exist)
try:
    mycursor.execute("CREATE DATABASE IF NOT EXISTS crud_python")
    print("Database Created or Already Exists")
except mysql.connector.Error as err:
    print(f"Database Creation Error: {err}")
    exit(1)
    
# Switch to the new database
try:
    conn.database = "crud_python"
except mysql.connector.Error as err:
    print(f"Switch Database Error: {err}")
    exit(1)
    
#STEP:3- Create a Table
try:
    mycursor.execute(
        """
        CREATE TABLE IF NOT EXISTS customers(
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(50) NOT NULL,
            email VARCHAR(50) NOT NULL,
            age INT
        )
        """
    )
    conn.commit()
    print("Table is created")
except mysql.connector.Error as err:
    print(f"Table Creation Error: {err}")
    exit(1)

#STEP:4-Insert new records into the "customers" table.
try:
    sql = "INSERT INTO customers (name, email, age) VALUES (%s, %s, %s)"
    val = [
        ("Anil", "anil@gmail.com", 40),
        ("Rahul", "rahul@gmail.com", 24),
        ("Parshv", "Parshv@gmail.com", 34)
    ]
    mycursor.executemany(sql, val)
    conn.commit()
    print(mycursor.rowcount, "records inserted successfully.")
except mysql.connector.Error as err:
    print(f"Error: {err}")
    conn.rollback()
    
#STEP:5.READ :select data from a table
try:
    mycursor.execute("SELECT * FROM customers")
    myresult = mycursor.fetchall()
    for row in myresult:
        print(row)
except mysql.connector.Error as err:
    print(f"Error: {err}")

for x in myresult:
    print(x[2])
    
#STEP:6.UPDATE :update data in a table
mycursor.execute("update customers set age=41 where id =3")
conn.commit()
print("updated")

#STEP:7.DELETE data from Table.
mycursor.execute("delete from customers where id = 1")
conn.commit()
print("deleted")

# Close the connection
conn.close()