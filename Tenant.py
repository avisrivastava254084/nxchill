import csv
import ast

class Tenant:

	fileName = "Owners.csv"

	def __init__(self, screens):
		self.screens = screens

	def search(self):
		matchList = []
		with open(self.fileName, 'rb') as csv_reader:
			reader = csv.reader(csv_reader)
			for row in reader:
				currDict = ast.literal_eval(row[0])
				if(self.screens <= currDict["availableScreens"]):
					matchList.append(currDict)
		print matchList

screens = input("Please enter the total no of screens you want: ")
ob = Tenant(screens)
ob.search()