def SqlToTable(cur):
    from prettytable import from_db_cursor as dbc


    x = "a"
    while x != "n":
        q = input("Enter the query:  ")
        cur.execute(q)
        table = dbc(cur)
        if table == None:
            print("done")
        else:
            print(table)
        x = input("type 'n' to stop or press enter:  ").lower()