import mysql.connector

def main():
  mydb = mysql.connector.connect(host="localhost", user="chasebernard8",
  passwd="", database="userlogin")

  username = raw_input("Please enter your username")
  passwd = raw_input("Please enter your password")

  add_user = ("INSERT INTO userlogin "
 "(username, password) VALUES (" + username + ", " + passwd + ")")

  mydb.commit()
  mydb.close()


if __name__ == "__main__":
  main()
