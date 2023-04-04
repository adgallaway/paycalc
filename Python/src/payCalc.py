def menu1():
    print("Select the frequency of pay")
    print("[1] Hourly")
    print("[2] Weekly")
    print("[3] BiWeekly")
    print("[4] Monthly")
    print("[5] Annually")
    frequency = int(input(":"))
    menu2(frequency)

def hourly(frequency): #Perform Calculation for Hourly Pay
    hourlyPay = 0
    if frequency == 1: hourlyPay = float(pay)
    elif frequency == 2: hourlyPay = float(pay / 40)
    elif frequency == 3: hourlyPay = float(pay / 80)
    elif frequency == 4: hourlyPay = float(((pay * 12) / 52) / 40)
    elif frequency == 5: hourlyPay =float((pay / 52) / 40)
    hourlyPay = round(hourlyPay, 2)
    print("Estimated Hourly pay: " + str(hourlyPay))

def weekly(frequency): #Perform Calculation for Weekly Pay
    if frequency == 1: weeklyPay = float(pay * 40)
    elif frequency == 2: weeklyPay = float(pay)
    elif frequency == 3: weeklyPay = float(pay / 2)
    elif frequency == 4: weeklyPay = float((pay * 12) / 52)
    elif frequency == 5: weeklyPay =float(pay / 52)
    weeklyPay = round(weeklyPay, 2)
    print("Estimated Weekly pay: " + str(weeklyPay))

def biweekly(frequency): #Perform Calculation for Bi-Weekly Pay
    if frequency == 1: biWeeklyPay = float(pay * 80)
    elif frequency == 2: biWeeklyPay = float(pay * 2)
    elif frequency == 3: biWeeklyPay = float(pay)
    elif frequency == 4: biWeeklyPay = float(((pay * 12) / 52) * 2)
    elif frequency == 5: biWeeklyPay =float((pay / 52) * 2)
    biWeeklyPay = round(biWeeklyPay, 2)
    print("Estimated Bi-Weekly pay: " + str(biWeeklyPay))

def monthly(frequency): #Perform Calculation for Monthly Pay
    if frequency == 1: monthlyPay = float(((pay * 40) * 52) / 12)
    elif frequency == 2: monthlyPay = float((pay * 52) / 12)
    elif frequency == 3: monthlyPay = float((pay * 26) / 12)
    elif frequency == 4: monthlyPay = float(pay)
    elif frequency == 5: monthlyPay = float(pay / 12)
    monthlyPay = round(monthlyPay, 2)
    print("Estimated Monthly Pay: " + str(monthlyPay))

def annually(frequency): #Perform Calculation for Annual Pay
    if frequency == 1: annualPay = float((pay * 40) * 52)
    elif frequency == 2: annualPay = float(pay * 52)
    elif frequency == 3: annualPay = float(pay * 26)
    elif frequency == 4: annualPay = float(pay * 12)
    elif frequency == 5: annualPay = float(pay)
    annualPay = round(annualPay, 2)
    print("Estimated Annual Pay: " + str(annualPay))

def menu2(frequency): #Select Which Calculation(s) to Perform
    if frequency >0 and frequency <6:
        print("Select how to calculate the pay of " + str(pay) + ": ")
        if frequency != 1: print("[1] Hourly")
        if frequency != 2: print("[2] Weekly")
        if frequency != 3: print("[3] Bi-Weekly")
        if frequency != 4: print("[4] Monthly")
        if frequency != 5: print("[5] Annually")
        selection = int(input(": "))
        case(selection, frequency)
    else:
        print("INVALID ENTRY!")
        menu1()
        
def case(selection, frequency) #Used instead of Match Case
    if selection == 0: #Perform All Calculations
        if frequency != 1: hourly(frequency)
        if frequency != 2: weekly(frequency)
        if frequency != 3: biweekly(frequency)
        if frequency != 4: monthly(frequency)
        if frequency != 5: annually(frequency)
    elif selection == 1: #Calculate Hourly Pay
        hourly(frequency)
    elif selection == 2: #Calculate Weekly Pay
        weekly(frequency)
    elif selection == 3: #Calculate Bi-Weekly Pay
        biweekly(frequency)
    elif selection == 4: #Calculate Monthly Pay
        monthly(frequency)
    elif selection == 5: #Calculate Annual Pay
        annually(frequency)
    else:
        print("\nINVALID ENTRY!! Please try again.\n")
        menu2(frequency)

#Main Body    
while True:
    print("\n")
    pay = float(input("Enter the pay amount:  "))
    menu1()
    print("\nPress ENTER to run again")
    print("Press Q to quit")
    y_n = input(":")
    if y_n == "q" or y_n == "Q":
        break



