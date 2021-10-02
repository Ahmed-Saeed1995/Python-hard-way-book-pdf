#defining a functions to run it later
def cheese_and_crackers(cheese_count,boxes_of_crackers):
    #printing arguments that got from functions and passed directly outside script
    print(f"You have {cheese_count} of cheeses!")
    print(f"you have {boxes_of_crackers} of boxes of crackers!")
    print("Man that`s enough for party!")
    print("Get a blanket.\n")
#a message of how we call the funcion first time
print("We just give the function numbers directly:")
#Calling the function first time
cheese_and_crackers(20,30)

#telling the user we used another way to run function
print("OR, we can use variables from our script:")
# a ssinging two variables to pass to funcions
amount_of_cheese = 10
amount_of_crackers = 50

#calling the function second time and pass to it the two variables
cheese_and_crackers(amount_of_cheese,amount_of_crackers)
#A message of excute the function third time with operation of math inside it
print("We can do even math inside it too:")
cheese_and_crackers(10 + 20, 5 + 6)
#A messafe of cxcute the function last way and combining variables and operation of math 
print("And we can combine the two, variabels and math:")
cheese_and_crackers(amount_of_cheese + 100,amount_of_crackers + 1000)