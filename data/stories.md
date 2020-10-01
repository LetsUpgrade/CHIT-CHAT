## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* about_coronavirus
  - utter_corona
  - utter_did_that_help
* affirm
  - utter_happy


## survey happy path
* greet
  - utter_greet
* affirm
  - health_form
  - form{"name":"health_form"}
  - form{"name":"null"}
  - utter_slot_values
* thankyou
  -utter_noworries
  -utter_goodbye

## survey stop
* greet
  - utter_greet
* affirm
  - health_form
  - form{"name":"health_form"}
* out_of_scope
  - utter_ask_continue
* deny
  - action_deactivate_form
  - form{"name":"null"}
  - utter_goodbye


## survey continue
* greet
  - utter_greet
* affirm
  - health_form
  - form{"name":"health_form"}
* out_of_scope
  - utter_ask_continue
* affirm
  - health_form
  - form{"name":"null"}
  - utter_slot_values

## ask health question from
* greet
  - utter_greet
* affirm
  - health_form
  - form{"name":"health_form"}
* ask_corona
  - utter_ask_corona
  - health_form
  - form{"name":"null"}
  - utter_goodbye
* ask_fever
  - utter_ask_fever
  - health_form
  - form{"name":"null"}
  - utter_goodbye


## no survey
* greet
  - utter_greet
* deny
  - utter_goodbye


## covid19
* about_covid-19
  - utter_covid19

## symptoms
* about_coronavirus_symptoms
  - utter_symptoms

## coronavirus_spread_air
* coronavirus_spread_air
    - utter_coronavirus_spread_air

## coronavirus_spread_feces
* coronavirus_spread_feces
  - utter_coronavirus_spread_feces

## coronavirus_spread_no_symptoms
* coronavirus_spread_no_symptoms
  - utter_coronavirus_spread_no_symptoms

## coronavirus_spread_animal_source
* coronavirus_spread_animal_source
  - utter_coronavirus_spread_animal_source

## coronavirus_protection_measures
* coronavirus_protection_measures
  - utter_coronavirus_protection_measures

## coronavirus_worry_covid19
* coronavirus_worry_covid19
  - utter_coronavirus_worry_covid19

## coronavirus_about_risk
* coronavirus_about_risk
  - utter_coronavirus_about_risk

## coronavirus_about_antibiotics
* coronavirus_about_antibiotics
  - utter_coronavirus_about_antibiotics

## coronavirus_about_vaccine
* coronavirus_about_vaccine
  - utter_coronavirus_about_vaccine

## coronavirus_about_mask
* coronavirus_about_mask
  - utter_coronavirus_about_mask

## coronavirus_about_incubation
* coronavirus_about_incubation
  - utter_coronavirus_about_incubation

## coronavirus_about_avoid
* coronavirus_about_avoid
  -utter_coronavirus_about_avoid
  
## say goodbye
* goodbye
  - utter_goodbye





## bot_asking_my_location
* corona_in_my_area
  - utter_type_location

## Vaccine_Updates
* vaccine_updates  
 - utter_vaccine_updates

## corona_recent_stats_path
* recent_stats
- action_recent_stats

## corona tracker path 
* corona_location_tracker
- action_corona_location_tracker

## facility type test center
* search_provider{"facility_type":"test center"}
  - action_facility_search

## facility type hospital
* search_provider{"facility_type":"hospital"}
  - action_facility_search

## facilty type Shelter
* search_provider{"facility_type":"shelter homes"}
  - action_facility_search

## facilty type free food
* search_provider{"facility_type":"free food"}
  - action_facility_search


## Simple_Corona_Predict
* do_i_have_corona
  - utter_ask_fever_yes_or_no
* fever_yes_or_no
  - utter_ask_cough_yes_or_no
* cough_yes_or_no
  - utter_ask_tiredness_yes_or_no
* tiredness_yes_or_no
  - utter_ask_loss_of_taste_and_smell_yes_or_no
* loss_of_taste_and_smell_yes_or_no
  - utter_ask_covid_contact
* covid_contact
  - utter_ask_travel_history
* travel_yes_or_no
  - action_corona_predict
  
