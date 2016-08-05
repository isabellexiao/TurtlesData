import csv
import wikipedia as w
import sys
import sqlite3
import csv

conn = sqlite3.connect ('TurtlesData.db')
c = conn.cursor()

def Characteristics():
	print('''Good choice!  Here you can learn about the characteristics of the turtles.
		Type 1 to learn the caraspace length of all female turtles.
		Type 2 to learn all the ages of the turtles found in pond 'ALM'.
		Type 3 to learn all the mass of the turtles captured by hoops.
		Or, you can quit by typing 4.''')

	characteristicschoice = (int(raw_input("Please choose a choice.  Type your choice here:")))
	while characteristicschoice != 4:
		if characteristicschoice == 1:
			query=c.execute("SELECT turtinfo.Sex,sizeinfo.Cara_Len from turtinfo JOIN sizeinfo ON turtinfo.T_ID=sizeinfo.T_ID where turtinfo.sex='F'")
			for row in list(query):
				asciiRow = []
				print row
				for item in row:
					if type(item) == type(u"hi"):
						asciiRow.append(item.encode('ascii'))
					else:
						asciiRow.append(item)
			print (asciiRow)
		if characteristicschoice == 2:
			query=c.execute("SELECT capinfo.Pond, turtinfo.Age from capinfo JOIN turtinfo ON capinfo.T_ID = turtinfo.T_ID where capinfo.Pond = 'ALM'")
			for row in list(query):
				asciiRow = []
				print row
				for item in row:
					if type(item) == type(u"hi"):
						asciiRow.append(item.encode('ascii'))
					else:
						asciiRow.append(item)
			print (asciiRow)
		if characteristicschoice == 3:
			query=c.execute("SELECT sizeinfo.Mass, capinfo.Trap_Type from sizeinfo JOIN capinfo ON sizeinfo.S_ID = capinfo.S_ID where capinfo.Trap_Type = 'Hoop'")
			for row in c.execute(query):
				asciiRow = []
				print row
				for item in row:
					if type(item) == type(u"hi"):
						asciiRow.append(item.encode('ascii'))
					else:
						asciiRow.append(item)
			print (asciiRow)

		
		# else:
		# 	print("That is not a valid option.  Please choose another.")
		characteristicschoice = int(raw_input("Please choose a choice.  Type your choice here:"))
	menu()

def menu():
	print("Welcome! Here you can learn about turtles!")
	print w.summary("Turtles", sentences = 3)
	print ('''Below are the available options that you can learn about:

		a. Characteristics 
	
		Or, type Q to quit!''')
	choice = raw_input("Please choose an option.  Type your option here: ")
	

	while choice.upper() != "Q":
		if choice.upper() == "A":
			Characteristics()
		
		else:
			print("Error. Please choose an available option.")
			choice = raw_input("Please choose another option.  Type your option here: ")
	
	sys.exit(0)
	print("Thank you for using our program!  Have a nice day!  Goodbye!")

	
menu()

 		