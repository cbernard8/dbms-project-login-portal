import mysql.connector

def main():
  mydb = mysql.connector.connect(host="localhost", user="user",
  passwd="Password1", database="userlogin")

  mycursor = mydb.cursor()

  username = raw_input("Please enter your username")
  passwd = raw_input("Please enter your password")

  add_user = ("INSERT INTO userlogin "
 "(id, username, password) VALUES (1, " + username + ", " + passwd + ")")

  mycursor.execute(add_user)

  mydb.commit()
  mycursor.close()
  mydb.close()


if __name__ == "__main__":
  main()
