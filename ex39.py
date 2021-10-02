#create a mapping to state to abbriviation

states = {'oregon':'OR','Florida':'FL','california':'CA',
         'New York':'NY','Michigan':'MI'}
         
#create a basic set of states and some cities in them

cities = {'CA':'san Francisco','MI':'Detroit','FL':'Jacksonville'}

#add some more cities
cities['NY'] = "New York"
cities['OR'] = "Portland"

#print out some cities
print('_' * 4)
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

#print some states
print('_' * 5)
print("Michigan`s abbreviation is: ",states['Michigan'])
print("Florida`s abbriviation is: ",states['Florida'])

#do it by using state the cities dict
print('_' * 6)
print("Michigan has: ",cities[states['Michigan']])
print("Florida has: ",cities[states['Florida']])

#print every state abbriviation
print('_' * 7)
for state, abbrv in list(states.items()):
    print(f"{state} is abbreviated {abbrv}")

#print avery city in state
print( '_' * 8)
for abbrv, city in list(cities.items()):
    print(f"{abbrv} has city {city}")
    
#now do both at the same time
print('_' * 9)
for state, abbrv in list(states.items()):
    print(f"{state} state is abbreviated {abbrv}")
    print(f"and has city {cities[abbrv]}")

print('_' * 10)
#safely get abbreviation by state that might not be there
state = states.get("Texas")
if not state:
    print("Soory, no Texus")

#get a city with a defult value
city = cities.get('TX','Does not exist')
print(f"The city of the state 'TX' is: {city}")