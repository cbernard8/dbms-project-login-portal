import mysql.connector

def main():
  mydb = mysql.connector.connect(host="localhost", user="chasebernard8",
  passwd="")

  username = raw_input("Please enter your username")
  passwd = raw_input("Please enter your password")

