from sys import argv

script, user_name , phone_number = argv
prompt ='**'

print(f"Hi {user_name}. I`m the {script} script.")
print("I`d like to ask tiy a few questions.")
print(f"Do you like me {user_name}.")
likes = input(prompt)

print(f"where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print("whai is your favorite subjects")
subject = input(prompt)

print(f"""
Alright, so you said {likes} about talking me.
You live in {lives}. Not sure where that is. Your phone number is {phone_number}.
And you have {computer} computer. And last things your favorite subject is: '{subject}'.
All Done Nice.
""")