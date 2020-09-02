import mysql.connector

def create_new_user(name, password, cursor, database):
  add_user = ("INSERT INTO user "
  "(username, password) VALUES (%s, %s)")

  cursor.execute(add_user,(name, password))


def delete_user(name, password, cursor, database):
  delete_user = ("DELETE FROM user "
                 "WHERE username = %s "
                 "AND password = %s")
  print "Deleting user with name " + name

  cursor.execute(delete_user, (name, password))
  
  
