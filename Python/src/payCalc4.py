#! /usr/bin/Python3

#Created by Aaron Gallaway (c)2023

import os
import time
import platform

def windows():
    os.system('cls')

def linux():
    os.system('clear')

def clearScreen(): #Function Clears the Screen
    if platform.system() == 'Windows':
        windows()
    elif platform.system() == 'Linux':
        linux()
    else:
        pass
    
def menu1():
    print("Select the frequency of pay")
    print("[1] Hourly")
    print("[2] Weekly")
    print("[3] BiWeekly")
    print("[4] Monthly")
    print("[5] Annually")
    frequency = input(':')
    frequency = int(frequency[:1]) #Takes only the first character entered
    menu2(frequency)

def menu2(frequency): #Select Which Calculation(s) to Perform
    clearScreen()
    if frequency >0 and frequency <6:
        print("Select how to calculate the pay of " + str(pay) + ": ")
        if frequency != 1: print("[1] Hourly")
        if frequency != 2: print("[2] Weekly")
        if frequency != 3: print("[3] Bi-Weekly")
        if frequency != 4: print("[4] Monthly")
        if frequency != 5: print("[5] Annually")
        selection = input(':')
        selection = int(selection[:1]) #Takes only the first character entered
        case(selection, frequency)
    else:
        clearScreen()
        print("INVALID ENTRY!")
        menu1()
        
def case(selection, frequency):
    match selection:
        case 0: #Perform All Calculations
            if frequency != 1: hourly(frequency)
            if frequency != 2: weekly(frequency)
            if frequency != 3: biweekly(frequency)
            if frequency != 4: monthly(frequency)
            if frequency != 5: annually(frequency)
        case 1: #Calculate Hourly Pay
            hourly(frequency)
        case 2: #Calculate Weekly Pay
            weekly(frequency)
        case 3: #Calculate Bi-Weekly Pay
            biweekly(frequency)
        case 4: #Calculate Monthly Pay
            monthly(frequency)
        case 5: #Calculate Annual Pay
            annually(frequency)
        case _: #Default if anything other than 0-5 is entered
            clearScreen()
            print("\nINVALID ENTRY!! Please try again.\n")
            time.sleep(2)
            menu2(frequency)


def hourly(frequency): #Perform Calculation for Hourly Pay
    match frequency:
        case 1: hourlyPay = float(pay)
        case 2: hourlyPay = float(pay / 40)
        case 3: hourlyPay = float(pay / 80)
        case 4: hourlyPay = float(((pay * 12) / 52) / 40)
        case 5: hourlyPay =float((pay / 52) / 40)
    #hourlyPay = round(hourlyPay, 2)
    text = "Estimated Hourly pay: {:.2f}"
    print(text.format(hourlyPay))

def weekly(frequency): #Perform Calculation for Weekly Pay
    match frequency:
        case 1: weeklyPay = float(pay * 40)
        case 2: weeklyPay = float(pay)
        case 3: weeklyPay = float(pay / 2)
        case 4: weeklyPay = float((pay * 12) / 52)
        case 5: weeklyPay =float(pay / 52)
    #weeklyPay = round(weeklyPay, 2)
    text = "Estimated Weekly pay: {:.2f}"
    print(text.format(weeklyPay))

def biweekly(frequency): #Perform Calculation for Bi-Weekly Pay
    match frequency:
        case 1: biWeeklyPay = float(pay * 80)
        case 2: biWeeklyPay = float(pay * 2)
        case 3: biWeeklyPay = float(pay)
        case 4: biWeeklyPay = float(((pay * 12) / 52) * 2)
        case 5: biWeeklyPay =float((pay / 52) * 2)
    #biWeeklyPay = round(biWeeklyPay, 2)
    text = "Estimated Bi-Weekly pay: {:.2f}"
    print(text.format(biWeeklyPay))

def monthly(frequency): #Perform Calculation for Monthly Pay
    match frequency:
        case 1: monthlyPay = float(((pay * 40) * 52) / 12)
        case 2: monthlyPay = float((pay * 52) / 12)
        case 3: monthlyPay = float((pay * 26) / 12)
        case 4: monthlyPay = float(pay)
        case 5: monthlyPay = float(pay / 12)
    #monthlyPay = round(monthlyPay, 2)
    text = "Estimated Monthly pay: {:.2f}"
    print(text.format(monthlyPay))

def annually(frequency): #Perform Calculation for Annual Pay
    match frequency:
        case 1: annualPay = float((pay * 40) * 52)
        case 2: annualPay = float(pay * 52)
        case 3: annualPay = float(pay * 26)
        case 4: annualPay = float(pay * 12)
        case 5: annualPay = float(pay)
    #annualPay = round(annualPay, 2)
    text = "Estimated Annual pay: {:.2f}"
    print(text.format(annualPay))

    
        
#Main Body

count = 0
while True:
    clearScreen()
    print("\n")
    try:
        pay = float(input("Enter the pay amount:  "))
    except:
        print('\n\nInvalid Entry!')
        count = count + 1
        if count < 3:
            time.sleep(2)
            continue
        else:
            print('\n*****OPERATION TERMINATED*****')
            time.sleep(2)
            break
        
    menu1()
    print("\n[C] To Continue")
    print("[Q] To Quit")
    y_n = input(':')
    y_n = y_n[:1] #Takes only the first character entered
    if y_n == "q" or y_n == "Q":
        break



