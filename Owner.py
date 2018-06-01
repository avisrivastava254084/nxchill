import csv
class Owner:
	fileName = "Owners.csv"
	response = {}
	def __init__(self, userEmailId, noOfScreens, availableScreens, message):
		self.userEmailId = userEmailId
		self.noOfScreens = noOfScreens
		self.availableScreens = availableScreens
		self.message = message
	def advertise(self):
		self.response["userEmailId"] = self.userEmailId
		self.response["noOfScreens"] = self.noOfScreens
		self.response["availableScreens"] = self.availableScreens
		self.response["message"] = self.message
		with open(self.fileName, 'a') as csv_file:
			writer = csv.writer(csv_file)
			writer.writerow([self.response])
userEmailId = raw_input("Please enter your email: ")
noOfScreens = int(input("Please enter total no of screens in your netflix account: "))
availableScreens = int(input("Please enter no of screens you want to rent: "))
message = raw_input("Please enter a message for your netflix buff: ")
ob = Owner(userEmailId, noOfScreens, availableScreens, message)
ob.register()