def personality(person1, person2, person3, password):
	print(f"the '{person1 }' account has password '{password}'")
	print(f"the '{person2 }' account has password '{password}'")
	print(f"the '{person3 }' account has password '{password}'")
	print("Laier they`re not the same passwords in real Games! \n")

print("calling th function first way")
print("I have 3 account of conquer games that has same password")
personality("Ninja","Trojan","Warrior","0123689447")

print("\ncalling the function second way")
person_one = input("input your charachter 1: ")
person_two = input("input your charachter 2: ")
person_three = input("input your charachter 3: ")
password_all = input("input the password of all account: ")

personality(person_one,person_two,person_three,password_all)

print("\ncall the function third way")
per1 = "Monk"
per2 = "pirate"
per3 = "windwalker"
PASS = "0129970735"
personality(per1,per2,per3,PASS)

print("\ncall the function fourth way")
personality(per1 +" master",per2  + " master",per3 + " master",PASS +" +20")

print("\ncall the function fifth way")
personality(input("the charachter1\t"),input("the charachter2\t"), input("the charachter3\t"),input("thier password\t"))

print("\ncall the function sixth way")
p1 = input("input the level of charachter warrior: ")
p2 = input("input the level of charachter Ninja: ")
p3 = input("input the level of charachter Trojan: ")
Pass_word = input("input their passeword: ")
personality("warrior " + "Level " +p1,"Ninja " + "Level " + p2 ,"Trojan " + "Level " + p3,Pass_word + " 012 or 017")

print("\ncall the function seventh way")
person_1 = input("the person one`s name is: ")
person_3 = input("the person two`s name is: ")
personality(person_1,"WinWalker" + " Master",person_3,"01299707635")

print("run function eighth time, ")
person_one1 = "T.strik "
person_two2 = "Archer "
person_three3 = "Twist "
password = input("Input shared password: ")
personality(person_one1 + input("input title of charachter: "),person_two2 + input("input title of charachter: "), person_three3 + input("Type of charachter: "),password)

print("\nrun the funcion nineth times!")
print("**** Combine All Ways ****")
charachter_two = "Monk saint"
charachter_three = input("Third charachter and the level in Game: ")
personality("Archer Master" + " Level 138",charachter_two + f" {p1}", charachter_three + " Level 140",input("THE PAASSWORD IS: ") + " or 0127")

print("\nAt this point this point might seem different run of functions")
print("run the function tenth times LAST RUN!")
print("Is the function printing the three arguments brefore input finction!")
personality("Ninja Secard Master ", "Trojan Secard Master","Warrior Secard Master", input("PASSWORDS: "))

