#Assining a variable car = 100
cars = 100
#Area inside a car
space_in_a_car = 4
#the persons who driving the car
drivers = 30
#amout of passengers who allowd to go in a car
passengers = 90
#cars not driven by drivers
cars_not_driven = cars - drivers
#worked car to drive
cars_driven = drivers
#capacity of carpool
carpool_capacity = cars_driven * space_in_a_car
#divide cars in each of sample of passengers
average_passengers_per_car = passengers / cars_driven

print("There are", cars , "cars avaliable")
print("There are only" , drivers , "drivers avaliable")
print("There will be", cars_not_driven ,"empty cars today")
print("We can transport", carpool_capacity ,"people today")
print("We have", passengers , "to carpool today")
print("We need to put about" , average_passengers_per_car ,"in each car.")