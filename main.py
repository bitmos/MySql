# import mysql.connector as mysql
#
# db = mysql.connect(
#     port="3306",
#     host="localhost",
#     user="root",
#     passwd="",
#     database="test"
# )
# cursor = db.cursor()
import mysql.connector as mysql
db = mysql.connect(
    port="3306",
    host="localhost",
    user="root",
    passwd="Kk@100202",
    database="test"
)
try:
      print("Connection successful")

except mysql.Error as e:
      print("Not connected ...")
#To create table
# cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
#
# sql = """create table employees(
#              employee_id int(3),
#              name varchar(15),
#              gender varchar(1),
#              email varchar(30),
#              primary key (employee_id)) engine=innodb"""
#
# cursor.execute(sql)
# print("Table created successfully")
# try:
#     print("Database connection success")
#
#     cur = cur.cursor()
#     cur.execute("DROP TABLE IF EXISTS EMPLOYEE")
#
#     sql = """create table employees(
#              employee_id int(3),
#              name varchar(15),
#              gender varchar(1),
#              email varchar(30),
#              primary key (employee_id)) engine=innodb"""
#
#     cur.execute(sql)
#     print("Table created successfully")
#
# except cur.Error as e:
#     print("Table creation problem")


# To Insert
# sql = "insert into employees (employee_id, name, gender, email) values(%s, %s, %s, %s)"
# value = (401,'Ahmad','M','ahmad@gmail.com')
# try:
#      cursor.execute(sql, value)
#      db.commit()
#      print("Insert success ...")
#
# except mysql.Error as e:
#      print("Insert error " + e)
# cursor.execute("SHOW DATABASES")
# databases = cursor.fetchall() ## it returns a list of all databases present
#
# ## printing the list of databases
# print(databases)
#
# ## showing one by one database
# for database in databases:
#     print(database)


# To Display
# sql = "select * from employees"
# try:
#     cursor.execute(sql)
#     results = cursor.fetchall()
#     for row in results:
#         employeeId = row[0]
#         name = row[1]
#         gender = row[2]
#         email = row[3]
#
#         print(employeeId, name, gender, email)
# except:
#     print("Fail")
# db.close()

# To search
# employeeId = 401
#
# sql = "select * from employees where employee_id =%s";
#
# try:
#     value = (employeeId,)
#     n = cursor.execute(sql, value)
#     row = cursor.fetchone()
#     print(row[0], row[1], row[2], row[3])
#
# except:
#     print("Unable to select the row ...")
#
# db.close()

#To update
# sql = "update employees set email = %s where employee_id = %s";
# value = ("johnxyz@gmail.com",401)
#
# try:
#      cursor.execute(sql, value)
#      db.commit()
#      print('Table updated successfully ...')
#
# except mysql.Error as e:
#      print("Unable to update table ..." + e)
#
# db.close()

#To Delete
# sql = "delete from employees where employee_id = %s";
# value = (102,)
#
# try:
#      cursor.execute(sql, value)
#      db.commit()
#      print('Row deleted successfully ...')
#
# except:
#      print("Unable to delete the row ...")
#
# db.close()

#tTo Count numver if rows
# sql = "select * from employees"
#
# try:
#      row_count = cursor.execute(sql)
#      print("row_count = ",row_count)
#
# except:
#      print("Unable to fetch data ...")
#
#
# db.close()

#to count the number of rows in employees table by using select count(*) from employees.
# sql = "select count(*) from employees"
#
# try:
#      cursor.execute(sql)
#      row_count = cursor.fetchone()[0]
#      print("row_count = ",row_count)
#
# except:
#      print("Unable to fetch data ...")
#
#
# db.close()

#To drop table
sql = "drop table if exists employees";

try:
     cursor.execute(sql)
     db.commit()
     print('Table dropped successfully ...')

except:
     print("Unable to drop the table/table not found")

db.close()

