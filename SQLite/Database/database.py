import sqlite3
#connect to database in python
conn = sqlite3.connect('customer.db')

#creating a table

#first we need to create a 'curser' -tells the database what it needs to do
c = conn.cursor()

#-----------------------------------create table------------------
# c.execute("""CREATE TABLE customers (
#     first_name text,
#     last_name text,
#     email text
# )""")


many_customers = [
    ('nikhil', 'ravi', 'nik@gmail.com'),
    ('neethu', 'ravi', 'nee@gmail.com'),
    ('nidhin', 'ravi', 'nid@gmail.com')
]

# # create a table
c.executemany("INSERT INTO customers values (?, ?, ?)", many_customers)



# fetching data
c.execute("SELECT * FROM customers WHERE email LIKE '%.com'")  #where keyword used to access objects have some specific values (like age<18,......)
# c.fetchone()
# c.fetchmany()
# print(c.fetchall())---------> 1st methode to fetch all


print("Name" + "\t\t\t" + " E-Mail")
print("------" + "\t\t\t" + " ------")
items = c.fetchall()# ---------> 2nd methode
# print(items)
for item in items:
    # print(item[0] + " " + item[1] + "\t\t " + item[2])
    print(item)
    # print(item[0])




# print("command executed sussessfully")
# sqlite database has only 5 datatypes where postgress.... database have dozens of datatypes
# null,integer,real, text, blob

# commit our command
conn.commit()

# close the connection
conn.close()












# c.execute("""CREATE TABLE customers (
#     first_name text,
#     last_name text,
#     email text
# )""")


# many_customers = [
#     ('nikhil', 'ravi', 'nik@gmail.com'),
#     ('neethu', 'ravi', 'nee@gmail.com'),
#     ('nidhin', 'ravi', 'nid@gmail.com')
# ]

# c.executemany("INSERT INTO customers values (?, ?, ?)", many_customers)   #? is a placeholder


