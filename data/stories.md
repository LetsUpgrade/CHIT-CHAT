## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot
  
## location+hospital_type+treatment_disease+schedule_an_appointment
* greet
  - action_bot_greet
* mood_great
  - action_ask_location
* taking_location
  - action_set_location
  - slot{"location":"Mumbai"}
  - utter_ask_hospital_type
* hospital_type{"location": "hyderabad", "hospital_type": "private hospitals"}
  - hospital_form
  - form{"name": "hospital_form"}
  - form{"name": null}
  - utter_ask_type_problem
* treatment_disease{"type_problem": "Diabeties"}
  - slot{"type_problem":"Diabeties"}
  - utter_ask_for_schedule_an_appointment
* Schedule_an_appointment
  - action_get_date_time
  - utter_slot_values
* goodbye
  - utter_goodbye
 
 
## location+symptoms+treatment_disease+tips_form
* greet
  - action_bot_greet
* mood_great
  - action_ask_location
* taking_location
  - action_set_location
  - slot{"location":"Mumbai"}
  - utter_ask_symptom_type
* telling_symptoms{"symptom_type":"headache"}
  - slot{"symptom_type":"headache"}
  - utter_ask_type_problem
* treatment_disease{"type_problem": "Diabeties"}
  - slot{"type_problem":"Diabeties"}
  - utter_ask_for_suggestions
* affirm
  - tips_form
  - form{"name": "tips_form"}
  - form{"name": null}
* goodbye
  - utter_happy
 
## location+appointment booking+name+phone_number+age
* greet
  - action_bot_greet
* mood_greet
  - utter_ask_for_booking_appointment
* Schedule_an_appointment
  - action_get_date_time
  - utter_slot_values
* affirm
  - hospital_form
  - form{"name": "hospital_form"}
  - form{"name": null}
  - utter_ask_for_name
* taking_name
  - action_get_name
  - utter_ask_phone_number
* taking_phone_number{"phone_number":"9486321896"}
  - slot{"phone_number":"9486321896"}
  - utter_ask_age
* age_group{"age":"18-40"}
  - slot{"age":"18-40"}
* deny
  - utter_goodbye
  
## taking_symptoms+age+giving_tips
* greet
  - utter_greet
* telling_symptoms{"symptom_type":"headache"}
  - slot{"symptom_type":"headache"}
  - utter_ask_age
* age_group{"age":"18-40"}
  - slot{"age":"18-40"}
* affirm
  - tips_form
  - form{"name": "tips_form"}
  - form{"name": null}
* goodbye
 - utter_goodbye
 
## deny location
* greet
  - action_bot_greet
* mood_great
  - utter_ask_location
* deny
  - utter_location_denied
* deny
  - utter_please_try_after_sometime
  - utter_goodbye
 
## appointement_booking
* greet
  - utter_greet
  - utter_ask_for_booking_appointment
* Schedule_an_appointment
  - action_get_date_time
  - utter_slot_values
* deny
  - utter_goodbye
  
## getting_name+phone_number+age+location+treatment_disease+appointment
 * greet
  - utter_greet
  - utter_ask_for_name
 * taking_name
  - action_get_name
  - utter_ask_phone_number
* taking_phone_number{"phone_number":"9486321896"}
  - slot{"phone_number":"9486321896"}
  - utter_ask_age
* age_group{"age":"18-40"}
  - slot{"age":"18-40"}
  - utter_ask_location
* taking_location
  - action_set_location
  - slot{"location":"Mumbai"}
  - utter_ask_type_problem
* treatment_disease{"type_problem": "Diabeties"}
  - slot{"type_problem":"Diabeties"}
  - action_show_hospitals
* affirm
  - hospital_form
  - form{"name": "hospital_form"}
  - form{"name": null}
  - utter_ask_for_booking_appointment
* Schedule_an_appointment
  - action_get_date_time
  - utter_slot_values
* goodbye
  - utter_goodbye
  
## symptoms+room_type+appointment
* greet
  - utter_greet
  - utter_ask_symptom_type
* telling_symptoms{"symptom_type":"headache"}
  - slot{"symptom_type":"headache"}
  - utter_ask_for_room_type
* Schedule_an_appointment
  - action_get_date_time
  - utter_slot_values
* goodbye
  - utter_goodbye
  
## hospital_type+treatment_disease+appointment+name+age+phone_number+location
* greet
 - utter_greet
* hospital_type{"location": "hyderabad", "hospital_type": "private hospitals"}
  - hospital_form
  - form{"name": "hospital_form"}
  - form{"name": null}
  - utter_ask_type_problem
* treatment_disease{"type_problem": "Diabeties"}
  - slot{"type_problem":"Diabeties"}
  - utter_ask_for_schedule_an_appointment
* Schedule_an _appointment
  - action_get_date_time
  - utter_slot_values
  - utter_ask_for_name
* taking_name
  - action_get_name
  - utter_ask_phone_number
* taking_phone_number{"phone_number":"9486321896"}
  - slot{"phone_number":"9486321896"}
  - utter_ask_age
* age_group{"age":"18-40"}
  - slot{"age":"18-40"}
  - utter_ask_location
* taking_location
  - action_set_location
  - slot{"location":"Mumbai"}
* goodbye
  - utter_goodbye
  
## medicine
* telling_symptoms{"symptom_type": "headache"}
  - slot{"symptom_type": "headache"}
  - action_medicine
  - slot{"symptom_type": {"mentions": [{"type": "symptom", "name": "Headache", "orth": "headache", "common_name": "Headache", "id": "s_21", "choice_id": "present"}]}}
* affirm
  - hospital_form
  - form{"name": "hospital_form"}
  - form{"name": null}
* goodbye
  - utter_goodbye
 
## appointment_booking+location+phone_number
* greet
  - utter_greet
  - utter_ask_for_appointment_booking 
* taking_location
  - action_set_location
  - slot{"location" : "Chennai"}
  - slot{"location" : "Pune"}
  - slot{"location" : "Assam"}
  - slot{"location" : "Bihar"}
  - slot{"location" : "Salem"}
  - utter_ask_phone_number
* taking_phone_number{"phone_number":"9486321896"}
  - slot{"phone_number":"9486321896"}
* goodbye
  - utter_goodbye
  
## search_hospital_type
* greet
  - utter_greet
* hospital_type{"location": "hyderabad", "hospital_type": "private hospitals"}
  - hospital_form
  - form{"name": "hospital_form"}
  - form{"name": null}
* thanks
   - utter_goodbye
   
## name + phone_number + query_type
* greet
   - utter_greet
* taking_name
 - action_get_name
* taking_phone_number{"phone_number" : "9486321896"}
   - slot{"phone_number" : "9486321896"}
* query_type
  - slot{"query_type" : "general query"}
  - slot{"query_type" : "appointment query"}
  - slot{"query_type" : "medicines query"}
* bye
   - utter_goodbye
   
## select_type + time_slots_form + online_payment
* greet
   - utter_greet
* select_type
  - slot{"select_type" : "book appointment"}
  - slot{"select_type" : "open hours"}
  - slot{"select_type" : "pharmacy"}
  - slot{"select_type" : "contact us"}
  - utter_ask_time_slots
* affirm
  - time_slots_form
  - form{"name": "hospital_form"}
  - form{"name": null}
  - slot{"time_slots" : "10:00 am"}
  - slot{"time_slots" : "11:00 am"}
  - slot{"time_slots" : "14:00 pm"}
  - slot{"time_slots" : "16:00 pm"}
* online_payment
  - slot{"online_payment" : "pay pal"}
  - slot{"online_payment" : "credit card"}
  - slot{"online_payment" : "pay at clinic"}
* thanks
   - utter_goodbye
   
## appointment_booking + location + treatment_disease + time _slots_form
* greet
 - utter_greet
 - utter_ask_for_appointment_booking 
* taking_location
  - action_set_location
  - slot{"location" : "Chennai"}
  - slot{"location" : "Pune"}
  - slot{"location" : "Assam"}
  - slot{"location" : "Bihar"}
  - slot{"location" : "Salem"}
* treatment_disease
  - slot{"type_problem" : "Orthopedics"}
  - slot{"type_problem" : "ENT"}
  - slot{"type_problem" : "General Surgery"}
  - slot{"type_problem" : "Dermatology"}
* affirm
  - time_slots_form
  - form{"name": "hospital_form"}
  - form{"name": null}
  - slot{"time_slots" : "10:00 am"}
  - slot{"time_slots" : "11:00 am"}
  - slot{"time_slots" : "14:00 pm"}
  - slot{"time_slots" : "16:00 pm"}
* bye
  - utter_goodbye
  
  
## hospital_+search + location
* greet 
   - utter_greet
   - utter_ask_hospital_type
* hospital_type{"location": "hyderabad", "hospital_type": "private hospitals"}
   - hospital_form
   - form{"name": "hospital_form"}
   - form{"name": null}
* inform{"location" : "Chennai"}
  - action_taking_location
* thanks
  - utter_goodbye
  
  
  

