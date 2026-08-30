print("Veterinary Patient Calculator")
print("------------------------------")
def assess_temperature(temperature):
    if temperature>39.5:
        return "Above expected range"
    elif temperature<37.5:
        return "Below expected range"
    else:
        return "Within Expected change"
def assess_heart_rate(heart_rate):
    if heart_rate>180:
        return "Above expected range"
    elif heart_rate<70:
        return "Below expected range"
    else:
        return "Within Expected change"
name= input("Enter animal name:")
species=input("Enter species(Dog/Cat):")
age=float(input("Enter age in years:"))
weight=float(input("Enter weight in kg:"))
temperature=float(input("Enter body temperature in C:"))
temperature_status=assess_temperature(temperature)
heart_rate=float(input("Enter heart rate:"))
heart_rate_status=assess_heart_rate(heart_rate)
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
