import sqlite3
#connect to database in python
conn = sqlite3.connect('customer.db')

c = conn.cursor()
#Drop Table
# c.execute("DROP TABLE customers")
# conn.commit

c.execute("SELECT rowid, * FROM customers ")



items = c.fetchall()                                                                                                                                            

for item in items:
    print(item)




# commit our command
conn.commit()

# close the connection
conn.close()