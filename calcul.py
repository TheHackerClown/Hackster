import math
print('Hello Mister')
print('I am a ...... Everything you want as Calculator')
print('What do you want:')
print('1. Currency Convertor \n2. Divider Which says everything \n3. Arithematic Calculator \n4. Temprature Convertor\n5. Speed Convertor \n6. Factorial Finder')
choice = input('Enter Your Choice [1/2/3/4/5/6]- ')
if choice == '1':
    currency1 = input('From Which Currency- ')
    currency2 = input('TO Which Currency- ')
    if currency1 == 'USD':
        if currency2 == 'INR':
            usd = 74.11
            usd = float(usd)
            currency3 = int(input('Enter The Amount In Dollar: '))
            currency4 = usd * currency3
            print('Your Currency in INR is: ',currency4)
    else:
        print('We Will Update The Database SO you can convert Currency.')
elif choice == '2':
    x = int(input('Enter The Divisor: '))
    y = int(input('Enter The Dividend: '))
    quo = y // x
    rema = y % x
    print('Divisor   : ',x)
    print('Dividend  : ',y)
    print('Remainder : ',rema)
    print('Quotient  : ',quo)
elif choice == '3':
    print('What DO you want to do \n1. Add \n2. Subtract \n3. Divide \n4. Multiply')
    epoxy = input('Enter Your Choice [1/2/3/4]: ')
    num1 = int(input('Enter the First Number: '))
    num2 = int(input('Enter the Second Number: '))
    if epoxy == '1':
        sum1 = num1 + num2
        print('Your Sum :',sum1)
    elif epoxy == '2':
        sub1 = num1 - num2
        print('Your Subtract: ',sub1)
    elif epoxy == '3':
        div1 = num1 / num2
        print('Your Divide: ',div1)
    elif epoxy == '4':
        multi1 = num1 * num2
        print('Your Multiply: ',multi1)
    else:
        print('Invalid Input')
elif choice == '4':
    temp1 = input('From Which Unit: ')
    if temp1 == 'F':
        temp2 = input('To Which Unit: ')
        if temp2 == 'C':
            feren = int(input('Enter the Temprature in Farenheit: '))
            cel = (feren - 32) * 5 / 9
            print('Temprature in Celsius: ',cel)
        elif temp2 == 'K':
            feren1 = int(input('Enter the Temprature in Farenheit: '))
            kel = (feren1 - 32) * 5/9 + 273.15
            print('Temprature in Kelvin: ',kel)
        else:
            print('Invalid Input')
    elif temp1 == 'C':
        temp3 = input('To Which Unit: ')
        if temp3 == 'F':
            cel1 = int(input('Enter Temprature in Celsius: '))
            feren1 = (cel1 * 9/5) + 32
            print('Temprature in Farenheit: ',feren1)
        elif temp3 == 'K':
            cel2 = int(input('Enter Temprature in Celsius: '))
            kel1 = cel2 + 273.15
            print('Temprature in Kelvin: ',kel1)
        else:
            print('Invalid Input')
    elif temp1 == 'K':
        temp4 = input('To Which Unit: ')
        if temp4 == 'F':
            kel5 = int(input('Enter Temprature in Kelvin: '))
            feren5 = (kel5 - 273.15) * 9 / 5 + 32
            print('Temprature in Farenheit: ',feren5)

        elif temp4 == 'C':
            kel6 = int(input('Enter Temprature in Kelvin: '))
            cel6 = kel6 - 273.15
            print('Your Temprature in Celsius: ',cel6)

        else:
            print('Invalid Input')
    else:
        print('We will update our database soon')
elif choice == '5':
    speedunit = input('From Which  Unit: ')
    if speedunit == 'Kmph':
        speedunit2 = input('To which Unit: ')
        if speedunit2 == 'mps':
            speed2 = int(input('Enter the Speed in KMPH: '))
            speed3 = speed2 * 5/18
            print('Speed in M/S: ',speed3)
        else:
            print('We will update our server')
    elif speedunit == 'mps':
        speedunit3 = input('To which Unit: ')
        if speedunit3 == 'kmph':
            speed67 = int('Enter the Speed M/s: ')
            speed57 = speed67 * 18 / 5
            print('Speed in Km/h: ',speed57)
    else:
        print('Invalid Input')
elif choice == '6':
	num2345 = int(input('Enter the number: '))
	print('Factorial: ',math.factorial(num2345))
else:
    print('Thanks for using me. \n Credits- Dhruv Pratap Singh,@TheHackerClown,ME-@dhruvpratap(both are my accounts)')


