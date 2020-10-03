# Importing the required libraries and Packages
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction 
from typing import Any, Text, Dict, List, Union

import requests
import json

import datetime
from datetime import date 
from datetime import timedelta 


class ActionCoronaLocationTracker(Action):
    """
    This is a Custom action Class which gives the covid-19 statistics when user inputs his location as State.
    """

    def name(self) -> Text:
        return "action_corona_location_tracker"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Getting the information from the api.
        response = requests.get("https://api.covid19india.org/data.json").json()
        
        # Using the tracker for finding the location typed by the user
        entities = tracker.latest_message['entities']
        state = " "
        for e in entities :
            if e['entity'] == "location" :
                state = e['value']
        
        # Validating the user input and giving the stats if user inputs correct State name.
        message = "Please enter correct State name !"
        for data in response["statewise"]:
            if (data["state"].lower() == state.lower()):
                # print(data)
                message = "Hey, These are the statistics of Cases in your area ! \n No of Active Cases :- " + data["active"] + "\n" + "No of Confirmed Cases :-  " + data["confirmed"] + "\n" + "No of Recovered Cases :-  " + data["recovered"] + "\n" + "No of Death Cases :-  " + data["deaths"] + "\n" + "The above details are latest updated on :-  " + data["lastupdatedtime"]
        

        dispatcher.utter_message(text= message )
        return []




class ActionCoronaTodaysStats(Action):
    """
    This is a Custom action Class which gives the recent covid-19 statistics of India.
    """

    def name(self) -> Text:
        return "action_recent_stats"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Getting the information from the api.
        response = requests.get("https://api.covid19india.org/data.json").json()
  
        # Get today's date 
        today = date.today() 

        # Yesterday date 
        yesterday = today - timedelta(days = 1) 
        
        # Converting the date from yyyy|mm|dd to dd Month. Ex:- 2020|10|02 to 02 October
        yesterday = str(yesterday).split("-")
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July','August', 'September', 'October', 'November', 'December']
        month = int(yesterday[1])
        result = ""
        result += yesterday[2]
        result +=" "
        result += months[month-1]
        result +=" "
        
        message = "Sorry ! Some internal error happened :}"
        
        # Fetching the Stats
        for data in response["cases_time_series"]:
            if data["date"] == result:
                message = "Here are Recent Covid-19 Updates of India !" + "\n"+ "The following corresponds to :-"+ data["date"] + "\n"+ "No of Confirmed Cases :-  " + data["dailyconfirmed"] + "\n" + "No of Recovered Cases :-  " + data["dailyrecovered"] + "\n" + "No of Death Cases :-  " + data["dailydeceased"]  + "\n" + "Head over the official WHO Website for Accurate Statistics here :- https://covid19.who.int/ "
        
       
        dispatcher.utter_message(text= message )
        return []




 # Getting the information from the api.
covid_facilities = requests.get('https://api.covid19india.org/resources/resources.json')
facilities_json= covid_facilities.json()


# Defining few functions which aid in giving the testcenters,hospitals,shelterhomes,freefoods availability by state 

def get_testcenters_by_state(state):
    facilities = []
    for res in facilities_json['resources']:
        if res['category'].lower() == 'CoVID-19 Testing Lab'.lower() and res['state'].lower() == state.lower():
            facilities.append(res['nameoftheorganisation']+", "+res['city']+", "+res['state']+", "+"Phone: "+res['phonenumber'])
    return facilities

def get_hospitals_by_state(state):
    facilities = []
    for res in facilities_json['resources']:
        if res['category'].lower() == 'hospitals and centers' and res['state'].lower()== state.lower():
            facilities.append(res['nameoftheorganisation']+", "+res['city']+", "+res['state']+", "+res['phonenumber'])
    return facilities

def get_shelterhomes_by_state(state):
    facilities = []
    for res in facilities_json['resources']:
        if res['category'].lower()== 'accommodation and shelter homes' and res['state'].lower()== state.lower():
            facilities.append(res['nameoftheorganisation']+", "+res['city']+", "+res['state']+", "+"Phone: "+res['phonenumber'])
    return facilities 


def get_freefoods_by_state(state):
    facilities = []
    for res in facilities_json['resources']:
        if (res['category'].lower() == 'free food' or res['category'].lower() == 'community kitchen') and res['state']== state.title():
            facilities.append(res['nameoftheorganisation']+", "+res['city']+", "+res['state']+", "+"Phone: "+res['phonenumber'])
    return facilities 



class ActionFacilitySearch(Action):
    """
    This is a Custom action Class which gives the details of available facilities in a given state like testcenters, hospitals, shelter homes, freefood availability.
    """
    def name(self) -> Text:
        return "action_facility_search"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            facility = tracker.get_slot("facility_type")
            location = tracker.get_slot("location")

            print("Tracked Facility: "+facility)
            print("Tracked Location: "+location)
            
            # Validating the type of facility user asks for and gives the details of free food availabilty.
            if facility == "free food":
                facilities_state = get_freefoods_by_state(location.title())
                if len(facilities_state) != 0:
                    allfacilities = "\n".join(facilities_state)
                    dispatcher.utter_message("Hey, here is the address of the {} facilities in {}:- \n {}".format(facility, location, allfacilities))
                else:
                    dispatcher.utter_message("Sorry! No {} found in {}".format(facility,location))
            
            # Validating the type of facility user asks for and gives the details of hospitals.
            if facility == "hospital":
                facilities_state = get_hospitals_by_state(location.title())
                if len(facilities_state) != 0:
                    allfacilities = "\n".join(facilities_state)
                    dispatcher.utter_message("Hey, here is the address of the {} facilities in {} :- \n {} ".format(facility, location, allfacilities))
                else:
                    dispatcher.utter_message("Sorry! No {} found in {}".format(facility,location))
            
            # Validating the type of facility user asks for and gives the details of testcenters.
            if facility == "test center":
                facilities_state = get_testcenters_by_state(location.title())
                if len(facilities_state) != 0:
                    allfacilities = "\n".join(facilities_state)
                    dispatcher.utter_message("Hey, here is the address of the {} facilities in {} :- \n {}".format(facility, location, allfacilities))
                else:
                    dispatcher.utter_message("Sorry! No {} found in {}".format(facility,location))
                    
            # Validating the type of facility user asks for and gives the details of shelter homes.
            if facility == "shelter home":
                facilities_state = get_shelterhomes_by_state(location.title())
                if len(facilities_state) != 0:
                    allfacilities = "\n".join(facilities_state)
                    dispatcher.utter_message("Hey, here is the address of the {} facilities in {}  :- \n {} ".format(facility, location, allfacilities))
                else:
                    dispatcher.utter_message("Sorry! No {} found in {}".format(facility,location))
            

        except:
            dispatcher.utter_message("Sorry ! Some internal error happened :}")
            
        return []




class ActionCoronaPredict(Action):
    """
    This is a Custom action Class which predicts whether a person has Covid-19 or not based on his responses to five questions.
    """
    def name(self) -> Text:
        return "action_corona_predict"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        try:
            # Getting the slot values.
            f=tracker.get_slot("fever")
            c=tracker.get_slot("cough")
            ti=tracker.get_slot("tiredness")
            c=tracker.get_slot("contact")
            tr=tracker.get_slot("travel")
            
           
            result_list=[f,c,ti,c,tr]
            
            # Counting for the presence of "yes" in slot values.
            threshold = 0
            for i in result_list :
                if "yes" in i.lower() :
                    threshold+=1
           
            print(threshold)
            
            # Giving the message based on number of times "yes" appeared.
            if (threshold== 5):
                dispatcher.utter_message("It is more likely that you have Covid-19.\n\n Better to go for a Covid Test and consult a doctor.")
            if (threshold==4):
                dispatcher.utter_message("I think you might have Covid-19. Better to go for a Covid test and consult doctor.")
            if (threshold==3):
                dispatcher.utter_message("I feel there is 50:50 chances that you are suffering from COVID-19.\n Better stay away in isolation for 3-5 days and if problem persists, consult a doctor.")
            if (threshold==2 or threshold==1) :
                dispatcher.utter_message("I think you do not have corona most probably. \n But it is better you stay in isolation for 6-7 days and if poblem persists, consult a doctor")
            if (threshold==0) : 
                dispatcher.utter_message("I feel you are alright. \n You do not have any symptoms of Covid-19. Stay safe!")

        except:
            dispatcher.utter_message("Sorry ! Some internal error happened :}")
            
        return []


