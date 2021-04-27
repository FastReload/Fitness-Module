from tkinter import *


def oxy():
    ox = int(input("Enter your pulse oxymeter reading: "))
    if ox >= 100:
        print("Enter a valid input")
        oxy()
    elif ox >= 89:
        print("YOUR PULSE OXYMETER READINGS ARE FINE AND YOUR OXYGEN LEVELS ARE HEALTHY")
    elif ox < 89:
        print("YOUR PULSE OXIMETER READINGS ARE LOW, PLEASE VISIT A DOCTOR ")


def BP():
    sys = int(input("enter your systolic pressure in terms of (mm of hg): "))
    dia = int(input("enter your diastolic pressure in terms of (mm of hg): "))

    def bp(s, d):
        if s == 120 and d == 80:
            print("You blood pressure is normal")
        elif s >= 121 and d >= 81:
            print("You have Hypertension, please visit a doctor")
        elif s <= 119 and d <= 79:
            print("You have Hypotension, please visit a doctor")

    bp(sys, dia)


def mcal():
    time = int(input('How many minutes were you exercising? '))  # if the user wishes to input time

    calories = 0
    for i in range(time):
        calories += 3.4

    print('You burned {} calories'.format(calories))

def scal():
    steps = int(input('How many steps have you walked? '))  # if the user wishes to input steps

    calories = 0
    for i in range(steps):
        calories += 0.4

    print('You burned {} calories'.format(calories))


def BMI():
    height = float(input("Input your height in centimeters: "))  # BMI calculator
    weight = float(input("Input your weight in kilograms: "))
    h = height / 100
    print("Your body mass index is: ", round(weight / h ** 2, 2))


def hrate():
    print('To enhance the accuracy of heartrate calculation, try to enter atleast 3 or more values')
    heartbeats = []
    heartbeat = int(input('Please enter your heartbeat '))
    heartbeats.append(heartbeat)
    user = input('Do you wish to make another entry yes/no ')
    while user == 'yes' or user == 'Yes' or user == 'y':
        heartbeat = int(input('Please enter your heartbeat '))
        heartbeats.append(heartbeat)
        user = input('Do you wish to make another entry yes/no ')
        if user == 'no' or user == 'No' or user == 'n':
            break
    bradychadia = 0
    tachychadia = 0

    if sum(heartbeats) / len(heartbeats) <= 40:
        print('Based on your average heartbeat, you seem to have bradycardia, please visit a DOCTOR immediately. ')
        bradychadia += 1

    elif sum(heartbeats) / len(heartbeats) > 100:
        tachychadia += 1
        print(
            'Based on your average heartbeat, you seem to have tachycardia,please visit a DOCTOR immediately. ')  # count the no. Of abnormal cases and display the result
    else:
        print('Based on your average heartbeat, your heartrate is normal ')
    if bradychadia >= 1 or tachychadia >= 1:
        print('Patient is at risk')

master = Tk()




def var_states():
    a = var1.get() #BMI
    b = var2.get()
    c = var3.get() #heart rate
    d = var4.get()
    e = var5.get() #BP
    f = var6.get()
    g = var7.get() #O2 level
    h = var8.get()
    i = var9.get() #calories
    j = var10.get()

    if a==1 and c==1 and e==1 and g==1 and i==1:
        scal()
        print('-'*50)
        mcal()
        print('-' * 50)
        hrate()
        print('-' * 50)
        BMI()
        print('-' * 50)
        BP()
        print('-' * 50)
        oxy()
        print('-' * 50)
    elif a==1:
        BMI()
    elif c==1:
        hrate()
    elif e==1:
        BP()
    elif g==1:
        oxy()
    elif i==1:
        scal()
        mcal()
    elif i==1 and a==1:
        scal()
        mcal()
        BMI()
    elif c==1 and e==1:
        hrate()
        BP()
    elif g==1 and i==1:
        oxy()
        scal()
        mcal()
    elif i==1 and c==1:
        scal()
        mcal()
        hrate()
    elif  i==1 and e==1:
        scal()
        mcal()
        BP()
    elif i==1 and g==1:
        scal()
        mcal()
        oxy()
    elif a==1 and c==1:
        BMI()
        hrate()
    elif a==1 and e==1:
        BMI()
        BP()
    elif a==1 and g==1:
        BMI()
        oxy()
    elif c==1and e==1:
        hrate()
        BP()
    elif c==1 and g==1:
        hrate()
        oxy()



master.geometry("400x400")

Label(master, text="FitnessFreaks").grid(row=0, sticky=S)

Label(master, text="Do you want to count the calories burnt ?").grid(row=2, sticky=W)
var9 = IntVar()
Checkbutton(master, text="Yes", variable=var9).grid(row=3, column=0, sticky=W)
var10 = IntVar()
Checkbutton(master, text="No", variable=var10).grid(row=3, column=1, sticky=W)

Label(master, text="Do you want to find your BMI?").grid(row=4, sticky=W)
var1 = IntVar()
Checkbutton(master, text="Yes", variable=var1).grid(row=5, column=0, sticky=W)
var2 = IntVar()
Checkbutton(master, text="No", variable=var2).grid(row=5, column=1, sticky=W)

Label(master, text="Do you want to find your heart rate ? ").grid(row=6, sticky=W)
var3 = IntVar()
Checkbutton(master, text="Yes", variable=var3).grid(row=7, column=0, sticky=W)
var4 = IntVar()
Checkbutton(master, text="No", variable=var4).grid(row=7, column=1, sticky=W)

Label(master, text="Do you want to find out about your Blood Pressure  ? ").grid(row=8, sticky=W)
var5 = IntVar()
Checkbutton(master, text="Yes", variable=var5).grid(row=9, column=0, sticky=W)
var6 = IntVar()
Checkbutton(master, text="No", variable=var6).grid(row=9, column=1, sticky=W)

Label(master, text="Do you want to find about your oxygen level ? ").grid(row=10, sticky=W)
var7 = IntVar()
Checkbutton(master, text="Yes", variable=var7).grid(row=11, column=0, sticky=W)
var8 = IntVar()
Checkbutton(master, text="No", variable=var8).grid(row=11, column=1, sticky=W)

Button(master, text='Quit', command=master.quit).grid(row=14, column=3, sticky=W, pady=4)
Button(master, text=' OK ', command=var_states).grid(row=14, column=0, sticky=W, pady=4)
mainloop()




