print("Veterinary Patient Calculator")
print("------------------------------")

def get_valid_number(prompt):
    while True:
        try:
            value=float(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid number")

def assess_temperature(temperature):
    if temperature>39.5:
        return "Above expected range"
    elif temperature<37.5:
        return "Below expected range"
    else:
        return "Within Expected change"
    
def assess_heart_rate(heart_rate,species):
    if species=="Dog":
        if heart_rate>120:
            return "Above expected range"
        elif heart_rate<70:
            return "Below expected range"
        else:
            return "Within Expected range"
    if species=="Cat":
        if heart_rate>140:
            return "Above expected range"
        elif heart_rate<120:
            return "Below expected range"
        else:
            return "Within Expected range"
        
name= input("Enter animal name:")
species=input("Enter species(Dog/Cat):")

age=get_valid_number("Enter age in years:")
        

weight=get_valid_number("Enter weight in kg:")
temperature=get_valid_number("Enter body temperature in C:")
temperature_status=assess_temperature(temperature)
heart_rate=get_valid_number("Enter heart rate:")
heart_rate_status=assess_heart_rate(heart_rate,species)
print()
print("Patient Information")
print("---------------------")
print("Name:",name)
print("Species:",species)
print("Age:",age,"years")
print("Weight:",weight,"kg")
print("Body Temperature:",temperature,"C")
print("Temperature status:",temperature_status)
print("Heart Rate:",heart_rate)
print("Heart rate status:",heart_rate_status)
