import database
#-----------------add one record------------
# database.add_one('leela', 'ravi', 'lee@r.com')

#-----------------delete one record------------
# database.delete_one('10')


#-----------------add many record------------
# names = [
#     ('aravind', 'sk', 'sk.com'),
#     ('anirudh', 'ms', 'ani@uh.com')
#     ]
# database.add_many(names)

database.email_lookup('lee@r.com')

# database.show_all()