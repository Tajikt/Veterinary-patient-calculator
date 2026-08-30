print("Veterinary Patient Calculator")
print("------------------------------")

reference_ranges={"Dog":{"heart_rate":(70,120),"respiratory_rate":(12,24)},
                   "Cat":{"heart_rate":(120,140),"respiratory_rate":(20,30)}}

def get_valid_number(prompt,minimum):
    while True:
        try:
            value=float(input(prompt))
            if value>=minimum:
             return value
            else:
                print("Value must be greater than or equal to", minimum)
        except ValueError:
            print("Please enter a valid number")

def assess_value(value,minimum,maximum):
    if value<minimum:
        return "Below expected range"
    elif value>maximum:
        return "Above expected range"
    else:
        return "Within Expected change"    

def assess_temperature(temperature):
    if temperature>39.5:
        return "Above expected range"
    elif temperature<37.5:
        return "Below expected range"
    else:
        return "Within Expected change"
    
def assess_heart_rate(heart_rate,species):
    if species not in reference_ranges:
        return "Unknown species"
    minimum,maximum= reference_ranges[species]["heart_rate"]
    if heart_rate>maximum:
        return "Above expected range"
    elif heart_rate<minimum:
        return "Below expected range"
    else:
        return "Within Expected range"
        
name= input("Enter animal name:")
species=input("Enter species(Dog/Cat):")
age=get_valid_number("Enter age in years:",0) 
weight=get_valid_number("Enter weight in kg:",0)
temperature=get_valid_number("Enter body temperature in C:",0)
temperature_status=assess_temperature(temperature)
heart_rate=get_valid_number("Enter heart rate:",0)
minimum,maximum=reference_ranges[species]["heart_rate"]
heart_rate_status=assess_value(heart_rate,minimum,maximum)
respiratory_rate=get_valid_number("Enter respiratory rate(bpm):",0)
minimum,maximum=reference_ranges[species]["respiratory_rate"]
respiratory_rate_status=assess_value(respiratory_rate,minimum,maximum)

print()
print("=======================================")
print(          "PTIENT SUMMARY")
print("=======================================")
print("Name:",name)
print("Species:",species)
print("Age:",age,"years")
print("Weight:",weight,"kg")

print()
print("Body Temperature:",temperature,"C")
print("Temperature status:",temperature_status)

print()
print("Heart Rate:",heart_rate)
print("Heart rate status:",heart_rate_status)

print()
print("Respiratory Rate:",respiratory_rate,"breath/min")
print("respiratory rate status:",respiratory_rate_status)

print("========================================")