## Most_Possible_Path
* greet
  - utter_greet
* about_coronavirus
  - utter_corona
* do_i_have_corona
  - utter_ask_fever_yes_or_no
* fever_yes_or_no
  - utter_ask_cough_yes_or_no
* cough_yes_or_no
  - utter_ask_tiredness_yes_or_no
* tiredness_yes_or_no
  - utter_ask_covid_contact
* covid_contact
  - utter_ask_travel_history
* travel_yes_or_no
  - action_corona_predict
* corona_in_my_area
  - utter_type_location 
* corona_location_tracker
  - action_corona_location_tracker  
* search_provider{"facility_type":"test center"}
  - action_facility_search
* search_provider{"facility_type":"hospital"}
  - action_facility_search
* coronavirus_protection_measures
  - utter_coronavirus_protection_measures
* recent_stats
  - action_recent_stats


## Simple_Corona_Predict
* do_i_have_corona
  - utter_ask_fever_yes_or_no
* fever_yes_or_no
  - utter_ask_cough_yes_or_no
* cough_yes_or_no
  - utter_ask_tiredness_yes_or_no
* tiredness_yes_or_no
  - utter_ask_covid_contact
* covid_contact
  - utter_ask_travel_history
* travel_yes_or_no
  - action_corona_predict
  

## Corona_Predict
* greet
  - utter_greet
* do_i_have_corona
  - utter_ask_fever_yes_or_no
* fever_yes_or_no
  - utter_ask_cough_yes_or_no
* cough_yes_or_no
  - utter_ask_tiredness_yes_or_no
* tiredness_yes_or_no
  - utter_ask_covid_contact
* covid_contact
  - utter_ask_travel_history
* travel_yes_or_no
  - action_corona_predict

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



## coronavirus_about_sanitizer
* coronavirus_about_sanitizer
 - utter_coronavirus_about_sanitizer


## coronavirus_precautive_vitamins
* coronavirus_precautive_vitamins
  - utter_coronavirus_precautive_vitamins

  ## spread_coronavirus
* spread_coronavirus
 - utter_spread_coronavirus

## coronavirus_children
* coronavirus_children
 - utter_coronavirus_children

## coronavirus_old_people
* coronavirus_old_people
  - utter_coronavirus_old_people

  ## coronavirus_old_adults_young
* coronavirus_old_adults_young
 - utter_coronavirus_old_adults_young

## prepare_for_outbreak
* prepare_for_outbreak
  - utter_prepare_for_outbreak

 ## coronavirus_test
* coronavirus_test
 - utter_coronavirus_test

## contact_tracing_corona_period
* contact_tracing_corona_period
 - utter_contact_tracing_corona_period

## funerals_corona
* funerals_corona
 - utter_funerals_corona

## coronavirus_cleaning_disinfection
* coronavirus_cleaning_disinfection
 - utter_coronavirus_cleaning_disinfection

## community_mitigation_corona
* community_mitigation_corona
 - utter_community_mitigation_corona

## corona_from_food_and_water
* corona_from_food_and_water
 - utter_corona_from_food_and_water

## treat_corona_home
* treat_corona_home
 - utter_treat_corona_home
