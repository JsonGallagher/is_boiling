unit = input("What unit are you using? ")
temp = int(input("What temp is the water? "))

boiling_temp_f = 212
boiling_temp_c = 100
boiling_temp_k = 373

if unit == 'f':
    if temp == boiling_temp_f:
        print("The water is boiling")
    else:
        print(f"The water is not boiling until {boiling_temp_f} degrees Farenheight.")
elif unit == 'c':
    if temp == boiling_temp_c:
        print("The water is boiling")
    else:
        print(f"The water is not boiling until {boiling_temp_c} degrees Celsius.")
elif unit == 'k': 
    if temp == boiling_temp_k:
        print("The water is boiling")
    else:
        print(f"The water is not boiling until {boiling_temp_k} degrees Kelvin.")
else:
    print("Not boiling")