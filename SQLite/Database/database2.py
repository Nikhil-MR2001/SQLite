import sqlite3
#connect to database in python
conn = sqlite3.connect('customer.db')

c = conn.cursor()


# ----------------------------------------update record------------------------------------------
# c.execute("""UPDATE customers SET first_name = 'ultra', last_name = 'pro', email = 'pro.com'
#             WHERE rowid = 1
# """)
# conn.commit()



# ----------------------------------------delete record-------------------------------------------
# c.execute("DELETE FROM customers WHERE rowid = 1")                                            # rowid makes a unique id to every rows(pk)
# conn.commit()



#-------------------------------------------ordering records---------------------------------------
#c.execute("SELECT rowid, * FROM customers ORDER by last_name")                                 # we can order the data in database by its last/first_name,rowis....
                                                                                                # we can also order by ascending/descending arder by ASC/DESC 
#-------------------------------------------AND/OR---------------------------------------
#c.execute("SELECT rowid, * FROM customers WHERE last_name = 'ravi' AND rowid = 6")             # we can use'OR' as well

#c.execute("SELECT rowid, * FROM customers LIMIT  3")                                            # LIMIT the records

#-------------------------------------------Query the db---------------------------------------
c.execute("SELECT rowid, * FROM customer ")

items = c.fetchall()                                                                                                                                            

for item in items:
    print(item)




# commit our command
conn.commit()

# close the connection
conn.close()
