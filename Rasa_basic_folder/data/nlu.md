## intent:affirm
- yes
- yep
- yeah
- indeed
- that's right
- thats right
- ok
- great
- right, thank you
- correct
- great choice
- sounds really good
- thanks
- please
- thank you
- thankyou
- yes. please
- yes. thank you
- yes. thankyou

## intent:deny
- no. thanks
- no
- i'm good
- no thankyou
- no thank you
- not now
- not today
- never

## intent:goodbye
- bye
- goodbye
- good bye
- stop
- end
- farewell
- Bye bye
- have a good one

## intent:greet
- hey
- how are you
- howdy
- hey there
- hello
- hi
- good morning
- good evening
- good afternoon
- dear sir
- hello
- hola

## intent:restaurant_search
- i'm looking for a place to eat
- I want to grab lunch
- I am searching for a dinner spot
- I am looking for some restaurants in [Delhi](location).
- I am looking for some restaurants in [Bangalore](location)
- I am looking for some [mexican](cuisine) restaurants in [Bangalore](location)
- I’m hungry. Looking out for some good [chinese](cuisine) restaurants in [Bangalore](location)
- show me [chinese](cuisine) restaurants
- show me [chines](cuisine:chinese) restaurants in the [New Delhi](location:Delhi)
- show me a [mexican](cuisine) place in the [centre](location)
- i am looking for an [indian](cuisine) spot called olaolaolaolaolaola
- search for restaurants
- anywhere in the [west](location)
- I am looking for [asian fusion](cuisine) food
- in [Gurgaon](location)
- in [Chandigad](location: Chandigarh)
- [South Indian](cuisine)
- [North Indian](cuisine)
- [Italian](cuisine)
- [Chinese](cuisine:chinese)
- [chinese](cuisine)
- [Lithuania](location)
- Oh, sorry, in [Italy](location)
- in [delhi](location)
- I am looking for a restaurant
- I am looking for some restaurants in [Mumbai](location)
- I am looking for [mexican indian fusion](cuisine)
- can you book a table in [rome](location) in a [moderate](price:medium) price range with [british](cuisine) food
- I'm looking for a [cheap](price:small) restaurant
- I'm looking for a [budget](price:small) restaurant
- I'm looking for a [low cost](price:small) restaurant
- I'm looking for an [economical](price:medium) restaurant
- I'm looking for a [fine dining](price:large) restaurant
- I'm looking for an [expensive](price:large) restaurant
- I'm looking for an [exclusive](price:large) restaurant
- [central](location) [indian](cuisine) restaurant
- please help me to find restaurants in [pune](location)
- Please find me a restaurant in [bangalore](location)
- Can you please find me a restaurant in [bangalore](location)
- [mumbai](location)
- [Chinese](cuisine:chinese)
- show me restaurants
- [mumbai](location)
- [Italian](cuisine)
- please find me [chinese](cuisine) restaurant in [delhi](location)
- can you find me a [chinese](cuisine) restaurant
- [delhi](location)
- please find me a restaurant in [ahmedabad](location)
- please show me a few [italian](cuisine) restaurants in [bangalore](location)
- I'm looking for a [chinese](cuisine) restaurant
- [delhi]{"entity": "location", "value": "New Delhi"}
- I'm looking for a [chinese](cuisine) restaraunt in [Bangalore](location)
- I'm looking for a [fine dining]{"entity": "price", "value": "large"} [mexican](cuisine) restaurant in [Mumbai](location)
- Can you email me a list of [fine dining]{"entity": "price", "value": "large"} [Mexican](cuisine) restaurants in [Mumbai](location) at [manohar.simons@gmail.com](email)?
- [Cheap]{"entity": "price", "value": "small"} [Mexican](cuisine) restaurants in [Mumbai](location)
- [Cheap]{"entity": "price", "value": "small"} [Chinese]{"entity": "cuisine", "value": "chinese"} restaurants in [Mumbai](location)
- [economical]{"entity": "price", "value": "medium"} [american](cuisine) restaurants in [Mumbai](location)

## intent:send_mail
- please send it to [abc@def.com](email)
- yes. Please send it to [ahbcdj@dkj.com](email)
- my email address is [ab12@it.org](email)
- [sbns@ms.co.uk](email)
- yes. [sdsh@sd.co.in](email)
- send it to [ahbcdj@dkj.com](email)

## synonym:bangalore
- Bengaluru
- blore

## synonym:chennai
- Madras

## synonym:New Delhi
- Delhi
- Dili
- Dilli

## synonym:Mumbai
- bombay
- mubaim
- mumbay

## synonym:Mysore
- Mysuru
- mysoru
- mysor

## synonym:Puducherry
- Pondicherry
- pondi

## synonym:Vadodara
- Baroda

## synonym:Vizag
- Vishakapatanam

## synonym:Surat
- Soorat

## synonym:Kochi
- Cochin

## synonym:Pune
- Poona

## synonym:Kolkata
- Calcutta

## synonym:Chandigarh
- chandigard
- chandighar
- Chandigad
- Chandigaad
- Chandighar

## synonym:chinese
- chines
- Chinese
- Chines

## synonym:medium
- moderate

## synonym:vegetarian
- veggie
- vegg
- veg

## regex:greet
- hey[^\s]*
