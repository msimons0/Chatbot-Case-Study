## interactive_story_complete_path
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_check_loc
    - slot{"check_resp": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_budget
* restaurant_search{"price": "medium"}
    - slot{"price": "medium"}
    - action_search_restaurants
    - utter_should_i_email
* affirm
    - utter_ask_email
* send_mail{"email": "manohar.simons@gmail.com"}
    - slot{"email": "manohar.simons@gmail.com"}
    - action_send_mail
    - utter_goodbye

## interactive_story_we_dont_operate
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
    - slot{"location": "Leh"}
    - action_check_loc
    - slot{"check_resp": false}
    - utter_we_dont_operate
    - utter_goodbye
    - export

## interactive_story_location
* greet
    - utter_greet  
* restaurant_search{"location": "New Delhi"}
    - slot{"location": "New Delhi"}
    - action_check_loc
    - slot{"check_resp": true}
    - utter_ask_budget
* restaurant_search{"price": "medium"}
    - slot{"price": "medium"}
    - action_search_restaurants
    - slot{"location": "New Delhi"}
    - utter_should_i_email
* affirm
    - utter_ask_email
* send_mail{"email": "manohar.simons@gmail.com"}
    - slot{"email": "manohar.simons@gmail.com"}
    - action_send_mail
    - slot{"email": "manohar.simons@gmail.com"}
    - utter_goodbye

## interactive_story_location_cuisine
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Bangalore"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Bangalore"}
    - action_check_loc
    - slot{"check_resp": true}
    - utter_ask_budget
    - action_search_restaurants
    - slot{"location": "Bangalore"}
    - utter_should_i_email
* affirm
    - utter_ask_email
* send_mail{"email": "manohar.simons@gmail.com"}
    - slot{"email": "manohar.simons@gmail.com"}
    - action_send_mail
    - slot{"email": "manohar.simons@gmail.com"}
    - utter_goodbye

## interactive_story_location_cuisine2
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Bangalore"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Bangalore"}
    - action_check_loc
    - slot{"check_resp": true}
    - utter_ask_budget
* restaurant_search{"price": "medium"}
    - slot{"price": "medium"}
    - action_search_restaurants
    - slot{"location": "Bangalore"}
    - utter_should_i_email
* deny
    - utter_goodbye

## interactive_story_location_cuisine3
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Bangalore"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Bangalore"}
    - action_check_loc
    - slot{"check_resp": false}
    - utter_we_dont_operate
    - utter_goodbye

## interactive_story_location_cuisine4
* greet
    - utter_greet
* restaurant_search{"cuisine": "american", "location": "Mumbai"}
    - slot{"cuisine": "american"}
    - slot{"location": "Mumbai"}
    - action_check_loc
    - slot{"check_resp": true}
    - utter_ask_budget
* restaurant_search{"price": "medium"}
    - slot{"price": "medium"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - utter_should_i_email
* affirm
    - utter_ask_email
* send_mail{"email": "manohar.simons@gmail.com"}
    - slot{"email": "manohar.simons@gmail.com"}
    - action_send_mail
    - slot{"email": "manohar.simons@gmail.com"}
    - utter_goodbye

## interactive_story_location_cuisine_budget
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Bangalore", "price": "medium"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "medium"}
    - slot{"location": "Bangalore"}
    - action_check_loc
    - slot{"check_resp": true}
* restaurant_search{"price": "medium"}
    - slot{"price": "medium"}
    - action_search_restaurants
    - slot{"location": "Bangalore"}
    - utter_should_i_email
* affirm
    - utter_ask_email
* send_mail{"email": "manohar.simons@gmail.com"}
    - slot{"email": "manohar.simons@gmail.com"}
    - action_send_mail
    - slot{"email": "manohar.simons@gmail.com"}
    - utter_goodbye

## interactive_story_location_price
* greet
    - utter_greet
* restaurant_search{"price": "small", "location": "Bangalore"}
    - slot{"price": "small"}
    - slot{"location": "Bangalore"}
    - action_check_loc
    - slot{"check_resp": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - action_search_restaurants
    - slot{"location": "Bangalore"}
    - utter_should_i_email
* affirm
    - utter_ask_email
* send_mail{"email": "manohar.simons@gmail.com"}
    - slot{"email": "manohar.simons@gmail.com"}
    - action_send_mail
    - slot{"email": "manohar.simons@gmail.com"}
    - utter_goodbye

## interactive_story_location_price1
* greet
    - utter_greet
* restaurant_search{"price": "small", "location": "Bangalore"}
    - slot{"price": "small"}
    - slot{"location": "Bangalore"}
    - action_check_loc
    - slot{"check_resp": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - action_search_restaurants
    - slot{"location": "Bangalore"}
    - utter_should_i_email
* deny
    - utter_goodbye

## interactive_story_location_price2
* greet
    - utter_greet
* restaurant_search{"price": "small", "location": "Bangalore"}
    - slot{"price": "small"}
    - slot{"location": "Bangalore"}
    - action_check_loc
    - slot{"check_resp": false}
    - utter_we_dont_operate
    - utter_goodbye

## interactive_story_cuisine_price
* greet
    - utter_greet
* restaurant_search{"price": "small", "cuisine": "American"}
    - slot{"price": "small"}
    - slot{"cuisine": "American"}
    - utter_ask_location
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_check_loc
    - slot{"check_resp": true}
    - action_search_restaurants
    - slot{"location": "Bangalore"}
    - utter_should_i_email
* affirm
    - utter_ask_email
* send_mail{"email": "manohar.simons@gmail.com"}
    - slot{"email": "manohar.simons@gmail.com"}
    - action_send_mail
    - slot{"email": "manohar.simons@gmail.com"}
    - utter_goodbye

## interactive_story_cuisine_price1
* greet
    - utter_greet
* restaurant_search{"price": "small", "cuisine": "American"}
    - slot{"price": "small"}
    - slot{"cuisine": "American"}
    - utter_ask_location
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_check_loc
    - slot{"check_resp": true}
    - action_search_restaurants
    - slot{"location": "Bangalore"}
    - utter_should_i_email
* deny
    - utter_goodbye

## interactive_story_cuisine_price2
* greet
    - utter_greet
* restaurant_search{"price": "small", "cuisine": "American"}
    - slot{"price": "small"}
    - slot{"cuisine": "American"}
    - utter_ask_location
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_check_loc
    - slot{"check_resp": false}
    - utter_we_dont_operate
    - utter_goodbye

## interactive_story_cuisine_price_location
* greet
    - utter_greet
* restaurant_search{"price": "large", "cuisine": "mexican", "location": "Mumbai"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "Mumbai"}
    - slot{"price": "large"}
    - action_check_loc
    - slot{"check_resp": true}
    - action_search_restaurants
    - utter_should_i_email
* affirm
    - utter_ask_email
* send_mail{"email": "manohar.simons@gmail.com"}
    - slot{"email": "manohar.simons@gmail.com"}
    - action_send_mail
    - utter_goodbye

## interactive_story_cuisine_price_location1
* greet
    - utter_greet
* restaurant_search{"price": "large", "cuisine": "mexican", "location": "Mumbai"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "Mumbai"}
    - slot{"price": "large"}
    - action_check_loc
    - slot{"check_resp": false}
    - utter_we_dont_operate
    - utter_goodbye

## interactive_story_cuisine_price_location2
* greet
    - utter_greet
* restaurant_search{"price": "large", "cuisine": "mexican", "location": "Mumbai"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "Mumbai"}
    - slot{"price": "large"}
    - action_check_loc
    - slot{"check_resp": true}
    - action_search_restaurants
    - utter_should_i_email
* deny
    - utter_goodbye

## interactive_story_cuisine_price_location3    
* greet
    - utter_greet
* restaurant_search{"price": "large", "cuisine": "Mexican", "location": "Mumbai", "email": "manohar.simons@gmail.com"}
    - slot{"cuisine": "Mexican"}
    - slot{"location": "Mumbai"}
    - slot{"price": "large"}
    - slot{"email": "manohar.simons@gmail.com"}
    - action_check_loc

## interactive_story_cuisine_price_location4
* greet
    - utter_greet
* restaurant_search{"price": "large", "cuisine": "Mexican", "location": "Mumbai", "email": "manohar.simons@gmail.com"}
    - slot{"cuisine": "Mexican"}
    - slot{"location": "Mumbai"}
    - slot{"price": "large"}
    - slot{"email": "manohar.simons@gmail.com"}
    - action_check_loc
    - slot{"check_resp": true}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - utter_should_i_email

## interactive_story_cuisine_price_location5
* greet
    - utter_greet
* restaurant_search{"price": "large", "cuisine": "Mexican", "location": "Mumbai", "email": "manohar.simons@gmail.com"}
    - slot{"cuisine": "Mexican"}
    - slot{"location": "Mumbai"}
    - slot{"price": "large"}
    - slot{"email": "manohar.simons@gmail.com"}
    - action_check_loc
    - slot{"check_resp": true}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - action_send_mail
    - slot{"email": "manohar.simons@gmail.com"}
    - utter_goodbye

## interactive_story_cuisine_price_location6
* restaurant_search{"price": "large", "cuisine": "Mexican", "location": "Mumbai", "email": "manohar.simons@gmail.com"}
    - slot{"cuisine": "Mexican"}
    - slot{"location": "Mumbai"}
    - slot{"price": "large"}
    - slot{"email": "manohar.simons@gmail.com"}
    - action_check_loc
    - slot{"check_resp": true}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - action_send_mail
    - slot{"email": "manohar.simons@gmail.com"}
    - utter_goodbye

## interactive_story_cuisine_price_location_email
* restaurant_search{"price": "large", "cuisine": "Mexican", "location": "Mumbai", "email": "manohar.simons@gmail.com"}
    - slot{"cuisine": "Mexican"}
    - slot{"location": "Mumbai"}
    - slot{"price": "large"}
    - slot{"email": "manohar.simons@gmail.com"}
    - action_check_loc
    - slot{"check_resp": true}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - action_send_mail
    - slot{"email": "manohar.simons@gmail.com"}
    - utter_goodbye

## interactive_story_cuisine_price_location8
* greet
    - utter_greet
* restaurant_search{"price": "small", "cuisine": "Mexican", "location": "Mumbai"}
    - slot{"cuisine": "Mexican"}
    - slot{"location": "Mumbai"}
    - slot{"price": "small"}
    - action_check_loc
    - slot{"check_resp": true}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - utter_should_i_email
* affirm
    - utter_ask_email
* send_mail{"email": "manohar.simons@gmail.com"}
    - slot{"email": "manohar.simons@gmail.com"}
    - action_send_mail

## interactive_story_cuisine_price_location8
* greet
    - utter_greet
* restaurant_search{"price": "small", "cuisine": "Mexican", "location": "Mumbai"}
    - slot{"cuisine": "Mexican"}
    - slot{"location": "Mumbai"}
    - slot{"price": "small"}
    - action_check_loc
    - slot{"check_resp": true}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - utter_should_i_email
* affirm
    - utter_ask_email
* send_mail{"email": "manohar.simons@gmail.com"}
    - slot{"email": "manohar.simons@gmail.com"}
    - action_send_mail

## interactive_story_cuisine_price_location9
* greet
    - utter_greet
* restaurant_search{"price": "small", "cuisine": "Mexican", "location": "Mumbai"}
    - slot{"cuisine": "Mexican"}
    - slot{"location": "Mumbai"}
    - slot{"price": "small"}
    - action_check_loc
    - slot{"check_resp": true}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - utter_should_i_email
* affirm
    - utter_ask_email
* send_mail{"email": "manohar.simons@gmail.com"}
    - slot{"email": "manohar.simons@gmail.com"}
    - action_send_mail

## interactive_story_cuisine_price_location10
* greet
    - utter_greet
* restaurant_search{"price": "small", "cuisine": "Mexican", "location": "Mumbai"}
    - slot{"cuisine": "Mexican"}
    - slot{"location": "Mumbai"}
    - slot{"price": "small"}
    - action_check_loc
    - slot{"check_resp": true}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - utter_should_i_email
* affirm
    - utter_ask_email
* send_mail{"email": "manohar.simons@gmail.com"}
    - slot{"email": "manohar.simons@gmail.com"}
    - action_send_mail

## interactive_story_cuisine_price_location11
* greet
    - utter_greet
* restaurant_search{"price": "small", "cuisine": "Mexican", "location": "Mumbai"}
    - slot{"cuisine": "Mexican"}
    - slot{"location": "Mumbai"}
    - slot{"price": "small"}
    - action_check_loc
    - slot{"check_resp": true}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - utter_should_i_email
* affirm
    - utter_ask_email
* send_mail{"email": "manohar.simons@gmail.com"}
    - slot{"email": "manohar.simons@gmail.com"}
    - action_send_mail

## interactive_story_cuisine_price_location12
* greet
    - utter_greet
* restaurant_search{"price": "small", "cuisine": "chinese", "location": "Mumbai"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Mumbai"}
    - slot{"price": "small"}
    - action_check_loc
    - slot{"check_resp": true}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - utter_should_i_email
* affirm
    - utter_ask_email
* send_mail{"email": "manohar.simons@gmail.com"}
    - slot{"email": "manohar.simons@gmail.com"}
    - action_send_mail
* restaurant_search{"price": "medium", "cuisine": "american", "location": "Mumbai"}
    - slot{"cuisine": "american"}
    - slot{"location": "Mumbai"}
    - slot{"price": "medium"}
    - action_check_loc
    - slot{"check_resp": true}
    - action_search_restaurants
    - slot{"location": "Mumbai"}

* greet
    - utter_greet
* restaurant_search{"cuisine": "american", "location": "Mumbai"}
    - slot{"cuisine": "american"}
    - slot{"location": "Mumbai"}
    - action_check_loc
    - slot{"check_resp": true}
    - action_search_restaurants
    - slot{"location": "Mumbai"}

* greet
    - utter_greet
* restaurant_search{"price": "medium", "cuisine": "american", "location": "Mumbai"}
    - slot{"cuisine": "american"}
    - slot{"location": "Mumbai"}
    - slot{"price": "medium"}
    - action_check_loc
    - slot{"check_resp": true}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - utter_should_i_email
* affirm
    - utter_ask_email
* send_mail{"email": "manohar.simons@gmail.com"}
    - slot{"email": "manohar.simons@gmail.com"}
    - action_send_mail
    - slot{"email": "manohar.simons@gmail.com"}
    - utter_goodbye

* greet
    - utter_greet
* restaurant_search{"location": "colombo"}
    - slot{"location": "colombo"}
    - action_check_loc
    - slot{"check_resp": false}
    - utter_we_dont_operate
    - utter_goodbye
* greet
    - utter_greet
* restaurant_search{"price": "large", "cuisine": "italian", "location": "chennai"}
    - slot{"cuisine": "italian"}
    - slot{"location": "chennai"}
    - slot{"price": "large"}
    - action_check_loc
    - slot{"check_resp": true}
    - action_search_restaurants
    - slot{"location": "chennai"}
    - utter_should_i_email
* affirm
    - utter_ask_email
* restaurant_search{"email": "manohar.simons@gmail.com"}
    - slot{"email": "manohar.simons@gmail.com"}
    - action_send_mail
    - slot{"email": "manohar.simons@gmail.com"}
    - utter_goodbye
* restaurant_search{"price": "medium", "cuisine": "american", "location": "Mumbai"}
    - slot{"cuisine": "american"}
    - slot{"location": "Mumbai"}
    - slot{"price": "medium"}
    - action_check_loc
    - slot{"check_resp": true}
    - action_search_restaurants
    - slot{"location": "Mumbai"}

* greet
    - utter_greet
* restaurant_search{"price": "medium", "cuisine": "american", "location": "Mumbai"}
    - slot{"cuisine": "american"}
    - slot{"location": "Mumbai"}
    - slot{"price": "medium"}
    - action_check_loc
    - slot{"check_resp": true}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - utter_should_i_email
* deny
    - utter_goodbye
* restaurant_search{"price": "medium", "cuisine": "american", "location": "Mumbai"}
    - slot{"cuisine": "american"}
    - slot{"location": "Mumbai"}
    - slot{"price": "medium"}
    - action_check_loc
    - slot{"check_resp": true}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - utter_should_i_email
* deny
    - utter_goodbye

* greet
    - utter_greet
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_check_loc
    - slot{"check_resp": true}
    - utter_ask_budget
    - slot{"price": "large"}
* restaurant_search{"price": "large"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - utter_should_i_email
* affirm
    - utter_ask_email
* restaurant_search{"email": "manohar.simons@gmail.com"}
    - slot{"email": "manohar.simons@gmail.com"}
    - action_send_mail
    - slot{"email": "manohar.simons@gmail.com"}
    - utter_goodbye

* greet
    - utter_greet
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_location
* restaurant_search{"location": "New Delhi"}
    - slot{"location": "New Delhi"}
    - action_check_loc
    - slot{"check_resp": true}
    - utter_ask_budget
* restaurant_search{"price": "small"}
    - slot{"price": "small"}
    - action_search_restaurants
    - slot{"location": "New Delhi"}
    - utter_should_i_email
* affirm
    - utter_ask_email
* restaurant_search{"email": "manohar.simons@gmail.com"}
    - slot{"email": "manohar.simons@gmail.com"}
    - action_send_mail
    - slot{"email": "manohar.simons@gmail.com"}
    - utter_goodbye

* restaurant_search{"location": "Chandigarh"}
    - slot{"location": "Chandigarh"}
    - action_check_loc
    - slot{"check_resp": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search
    - action_search_restaurants
    - slot{"location": "Chandigarh"}
    - utter_should_i_email
* deny
    - utter_goodbye

