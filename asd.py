from getpass import getpass
from mysql.connector import connect, Error

#connection check
try:
    with connect(
        host="localhost",
        user=input("Имя пользователя: "),
        password=getpass("Пароль: "),
    ) as connection:
        print(connection)
except Error as e:
    print(e)


'''pwd manager'''

#database
pwd = "CREATE DATABASE IF NOT EXISTS pwd_manager"

#user input
login = input("Login: ")
password = input("password")
site = input("Cite: ")

#table for manager(console version)

create_pwd = """
CREATE TABLE pwd_manager(
    id INT AUTO_INCREMENT PRIMARY KEY,
    login VARCHAR(100),
    password VARCHAR(100),
    site VARCHAR(100),
)
"""

with connection.cursor() as cursor:
    cursor.execute(create_pwd)
    connection.commint()
print(create_pwd)
