import sys
import mysql.connector
import user_functions


def main(argc, argv):
  mydb = mysql.connector.connect(host="localhost", user="root",
  passwd="password", database="userlogin")

  mycursor = mydb.cursor()

  username = raw_input("Please enter your username: ")
  passwd = raw_input("Please enter your password: ")

  user_functions.create_new_user(username, passwd, mycursor, mydb)

  if argc == 2 and argv[1] == "-d":
    user_functions.delete_user(username, passwd, mycursor, mydb)

  mydb.commit()
  mycursor.close()
  mydb.close()


if __name__ == "__main__":
  main(len(sys.argv), sys.argv)
