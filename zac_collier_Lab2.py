prompt = input('What units of measurement would you like to convert?\n\
    \n[1]: Miles to kilometers\
    \n[2]: Fahrenheit to Celsius\
    \n[3]: Gallons to liters\
    \n[4]: Pounds to kilograms\
    \n[5]: Inches to centimeters\n\
    \nEnter your selection: ')

if int(prompt) > 5:
    selection = input('Please provide a valid input.')
if prompt == '1':
    selection = input('How many miles? \n')
    convert = float(selection)
    km = convert * 1.6
    print(selection + ' miles is ' + str(km) + ' kilometers.')
if prompt == '2':
    selection = input('How many degrees? \n')
    convert = float(selection)
    deg = (convert - 32) * 5 / 9
    print(selection + ' degrees Fahrenheit is ' + str(deg) + ' degrees Celsius.')
if prompt == '3':
    selection = input('How many gallons? \n')
    convert = float(selection)
    liters = convert * 3.9
    print(selection + ' gallons is ' + str(liters) + ' liters.')
if prompt == '4':
    selection = input('How many pounds? \n')
    convert = float(selection)
    kg = convert * 1.6
    print(selection + ' pounds is ' + str(kg) + ' kilograms.')
if prompt == '5':
    selection = input('How many inches? \n')
    convert = float(selection)
    cm = convert * 2.54
    print(selection + ' inches is ' + str(cm) + ' centimeters.')
