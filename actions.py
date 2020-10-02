from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction 

from typing import Any, Text, Dict, List, Union

import requests
import json



class ActionCoronaLocationTracker(Action):

    def name(self) -> Text:
        return "action_corona_location_tracker"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        response = requests.get("https://api.covid19india.org/data.json").json()
         
        entities = tracker.latest_message['entities']
        state = " "
        for e in entities :
            if e['entity'] == "location" :
                state = e['value']
        
        message = "Please enter correct State or City name !"
        for data in response["statewise"]:
            if (data["state"].lower() == state.lower()):
                # print(data)
                message = "Hey, These are the statistics of Cases in your area ! \n No of Active Cases :- " + data["active"] + "\n" + "No of Confirmed Cases :-  " + data["confirmed"] + "\n" + "No of Recovered Cases :-  " + data["recovered"] + "\n" + "No of Death Cases :-  " + data["deaths"] + "\n" + "The above details are latest updated on :-  " + data["lastupdatedtime"]
        

        dispatcher.utter_message(text= message )
        return []




class ActionCoronaTodaysStats(Action):

    def name(self) -> Text:
        return "action_recent_stats"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        response = requests.get("https://api.covid19india.org/data.json").json()
        

        import datetime
        from datetime import date 
        from datetime import timedelta 

        # Get today's date 
        today = date.today() 

        # Yesterday date 
        yesterday = today - timedelta(days = 1) 

        yesterday = str(yesterday).split("-")

        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July','August', 'September', 'October', 'November', 'December']

        month = int(yesterday[1])

        result = ""
        result += yesterday[2]
        result +=" "
        result += months[month-1]
        result +=" "

        print(result)
        message = "Sorry ! Some internal error happened :}"
        for data in response["cases_time_series"]:
            if data["date"] == result:
                message = "Here are Recent Covid-19 Updates of India !" + "\n"+ "The following corresponds to :-"+ data["date"] + "\n"+ "No of Confirmed Cases :-  " + data["dailyconfirmed"] + "\n" + "No of Recovered Cases :-  " + data["dailyrecovered"] + "\n" + "No of Death Cases :-  " + data["dailydeceased"]  + "\n" + "Head over the official WHO Website for Accurate Statistics here :- https://covid19.who.int/ "
        
       
        dispatcher.utter_message(text= message )
        return []





covid_facilities = requests.get('https://api.covid19india.org/resources/resources.json')
facilities_json= covid_facilities.json()


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

            if facility == "free food":
                facilities_state = get_freefoods_by_state(location.title())
                if len(facilities_state) != 0:
                    allfacilities = "\n".join(facilities_state)
                    dispatcher.utter_message("Hey, here is the address of the {} facilities in {}:- \n {}".format(facility, location, allfacilities))
                else:
                    dispatcher.utter_message("Sorry! No {} found in {}".format(facility,location))
            
            if facility == "hospital":
                facilities_state = get_hospitals_by_state(location.title())
                if len(facilities_state) != 0:
                    allfacilities = "\n".join(facilities_state)
                    dispatcher.utter_message("Hey, here is the address of the {} facilities in {} :- \n {} ".format(facility, location, allfacilities))
                else:
                    dispatcher.utter_message("Sorry! No {} found in {}".format(facility,location))
            
            if facility == "test center":
                facilities_state = get_testcenters_by_state(location.title())
                if len(facilities_state) != 0:
                    allfacilities = "\n".join(facilities_state)
                    dispatcher.utter_message("Hey, here is the address of the {} facilities in {} :- \n {}".format(facility, location, allfacilities))
                else:
                    dispatcher.utter_message("Sorry! No {} found in {}".format(facility,location))
            
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

    def name(self) -> Text:
        return "action_corona_predict"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        try:
            x1=tracker.get_slot("fever")
            x2=tracker.get_slot("cough")
            x3=tracker.get_slot("tiredness")
            x4=tracker.get_slot("contact")
            x5=tracker.get_slot("travel")

            result_list=[x1,x2,x3,x4,x5]
            print(result_list)
            threshold = 0
            for i in result_list :
                if "yes" in i.lower() :
                    threshold+=1
           
            print(threshold)

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


