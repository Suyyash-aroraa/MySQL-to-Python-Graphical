import mysql.connector as msc
from prettytable import from_db_cursor as dbc

mydb=msc.connect(host='LocalHost', user='root', password='12345678')

cur=mydb.cursor()
x = "a"
while x!="n":
    q = input("Enter the query:  ")
    cur.execute(q)
    table = None
    table = dbc(cur)
    if table == None:
        print("done")
    else:
        print(table)
    x = input("type 'n' to stop or press enter:  ").lower()


