name = 'Zed A,shaw'
age = 35 #not a lie
height = 74 * 2.54 #centimeters
weight = 180 / 2.205#kilograms
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let`s talk about {name}")
print(f"He`s {round(height)} centimeters tall.")
print(f"He`s {round(weight)} kilogram heavy.")
print("Actually that`s not too heavy.")
print(f"He`s got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

#this line is tricky. to try to get is exactly right
total = age + height + weight
print(f"If I add {age}, {round(height)}, and {round(weight)} I get {round(total)}.")