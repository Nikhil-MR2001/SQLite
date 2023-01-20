import sqlite3
def show_all():
    # establishin a connection to a database
    conn = sqlite3.connect('customer.db')
# creating a cursor
    c = conn.cursor()




    # query the database
    c.execute("SELECT rowid,* from customers")


    items = c.fetchall()
    for item in items:
        print(item)


    # print("heyy")
    conn.commit()
    conn.close()

def add_one(first, last, email):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()

    c.execute ("INSERT INTO customers VALUES (?, ?, ?)",(first, last, email))
    conn.commit()
    conn.close()

def add_many(list):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()

    c.executemany ("INSERT INTO customers VALUES (?, ?, ?)",(list))
    conn.commit()
    conn.close()




def delete_one(id):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()

    c.execute("DELETE from customers  WHERE rowid = (?)", id)
    conn.commit() 
    conn.close()


def email_lookup(email):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()

    c.execute("SELECT * from customers  WHERE email = (?)", (email,))
    items = c.fetchall()
    for item in items:
        print(item)
        
    conn.commit() 
    conn.close()

