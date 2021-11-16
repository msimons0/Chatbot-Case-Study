# Standard library imports.
from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Related third party imports.
from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import pandas as pd

ZomatoData = pd.read_csv('zomato.csv')
ZomatoData = ZomatoData.drop_duplicates().reset_index(drop=True)
WeOperate = ['New Delhi', 'Gurgaon', 'Noida', 'Faridabad', 'Allahabad', 'Bhubaneshwar', 'Mangalore', 'Mumbai', 'Ranchi', 'Patna', 'Mysore', 'Aurangabad', 'Amritsar', 'Puducherry', 'Varanasi', 'Nagpur', 'Vadodara', 'Dehradun', 'Vizag', 'Agra', 'Ludhiana', 'Kanpur', 'Lucknow', 'Surat', 'Kochi', 'Indore', 'Ahmedabad', 'Coimbatore', 'Chennai', 'Guwahati', 'Jaipur', 'Hyderabad', 'Bangalore', 'Nashik', 'Pune', 'Kolkata', 'Bhopal', 'Goa', 'Chandigarh', 'Ghaziabad', 'Ooty', 'Gangtok', 'Shimla']

def RestaurantSearch(City, Cuisine, Price):
	cost_lower = 0
	cost_upper = 1000000
	if Price=="small":
		cost_upper = 300
	elif Price=="medium":
		cost_lower = 300
		cost_upper = 600
	elif Price=="large":
		cost_lower = 600
	print(str(cost_lower) + "-" + str(cost_upper))

	data = ZomatoData[
        (ZomatoData.City.apply(lambda x: City.lower() in x.lower())) &
        (ZomatoData.Cuisines.apply(lambda x: Cuisine.lower() in x.lower())) &
        (ZomatoData['Average Cost for two'] >= cost_lower) &
        ((ZomatoData['Average Cost for two'] < cost_upper) if cost_upper else True)
    ].sort_values(by='Aggregate rating', ascending=False)
	#TEMP = ZomatoData[
	#	(ZomatoData['Average Cost for two'].apply(lambda x: (x >= lower & x< upper)))]
		#(ZomatoData['Cuisines'].apply(lambda x: Cuisine.lower() in x.lower())) & 
		#(ZomatoData['City'].apply(lambda x: City.lower() in x.lower())) &
	#TEMP =  TEMP[['Restaurant Name','Address','Average Cost for two','Aggregate rating']]
	#return TEMP.sort_values(by=['Aggregate rating'], ascending=False)
	return data[['Restaurant Name', 'Address', 'Average Cost for two', 'Aggregate rating']]

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'

	def run(self, dispatcher, tracker, domain):
		#config={ "user_key":"f4924dc9ad672ee8c4f8c84743301af5"}
		OKCYAN = '\033[96m'
		OKBLUE = '\033[94m'
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		price = tracker.get_slot('price')
		results = RestaurantSearch(City=loc, Cuisine=cuisine, Price=price)
		response=""
		if results.shape[0] == 0:
			response= "no results"
		else:
			response = "I found the following restraunts:\n\n"
			for restaurant in RestaurantSearch(loc, cuisine, price).iloc[:10].iterrows():
				restaurant = restaurant[1]
				response=response + F"{OKCYAN}{restaurant['Restaurant Name']}{OKBLUE} at {OKCYAN}{restaurant['Address']}{OKBLUE} has been rated {OKCYAN}{restaurant['Aggregate rating']}{OKBLUE}⭐️ with average cost {OKCYAN}Rs.{restaurant['Average Cost for two']}{OKBLUE}.\n\n"

		dispatcher.utter_message(response)
		return [SlotSet('location',loc)]

class ActionSendMail(Action):
	def name(self):
		return 'action_send_mail'

	@staticmethod
	def sendmail(receiver_address,response):
		#The mail addresses and password
		sender_address = 'restaurant.finder.bot@gmail.com'
		#Setup the MIME
		message = MIMEMultipart()
		message['From'] = sender_address
		message['To'] = receiver_address
		message['Subject'] = 'Your restaurant search results'   #The subject line
		#The body and the attachments for the mail
		message.attach(MIMEText(response, 'plain'))
		#Create SMTP session for sending the mail
		session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
		session.starttls() #enable security
		session.login(sender_address, 'bot.finder.restaurant') #login with mail_id and password
		text = message.as_string()
		session.sendmail(sender_address, receiver_address, text)
		session.quit()
		
	def run(self, dispatcher, tracker, domain):
		location = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		price = tracker.get_slot('price')
		mailID = tracker.get_slot('email')
		response = self.getResults(location, cuisine, price)
		self.sendmail(mailID, response)
		return [SlotSet('email', mailID)]

	@staticmethod
	def getResults(location, cuisine, price):
		results = RestaurantSearch(City=location, Cuisine=cuisine, Price=price)
		if results.shape[0] != 0:
			response = "I found the following restraunts:\n\n"
			for restaurant in RestaurantSearch(location, cuisine, price).iloc[:10].iterrows():
				restaurant = restaurant[1]
				response=response + F"{restaurant['Restaurant Name']} at {restaurant['Address']} has been rated {restaurant['Aggregate rating']}⭐️ with average cost Rs.{restaurant['Average Cost for two']}.\n\n"
		return response

class ActionCheckLocation(Action):
	def name(self):
		return 'action_check_loc'
	
	def run(self, dispatcher, tracker, domain):
		location = tracker.get_slot('location')
		print("Location: " + location)
		print("Operate: " + str(location.lower() in (city.lower() for city in WeOperate)))
		return [SlotSet('check_resp', location.lower() in (city.lower() for city in WeOperate))]
