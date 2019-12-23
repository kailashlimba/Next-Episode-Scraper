from UserInput import *
from database import *

def main:
	user_email = input("Email address: ")
	user_series = input("TV Series: ")

	user = UserDetails(user_email,user_series)
	message = ''

	database  = DatabaseEntry(config.DB_USERNAME,config.DB_PASSWORD,"testing")
	database.createTable("versionbeta")
	database.insertInto("versionbeta",user_email,user_series)
	



if __name__ =="__main__":
	main()