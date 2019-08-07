bal = [1000,4000,7000]
username = ['abc','def','ghi']
password = [111,222,333]

while True:
    a = input('Enter the username')
    ind = username.index(a)
    x=1
    if a in username:
        b = int(input('Enter the password'))
        if b in password and password.index(b) == ind:
            print ('Login Successful :) ')
            x = 0
        else:
            print('Wrong password :( ')
    else:
        print('Username does not exist')
    c = 0 
    if x == 0:
        c=int(input('Enter the choice of operation \n 1 for withdrawl\n 2 for deposit \n 3 for balance check \n 4 to change the pin \n 5 to EXIT'))
        if c == 1:
            amt = int(input('Enter the amount to be withdrawn = '))
            if amt < bal[ind]:
                bal[ind] = bal[ind] - amt
                print('Updated balance = '+str(bal[ind]))
            else:
                print ('Insufficient balance')
        elif c == 2:
            dep = int(input('Entr the amount to be deposited = '))
            bal[ind] = bal[ind] + dep
            print ('Updated balance = '+str(bal[ind]))
        elif c == 3:
            print('Current balance is ='+str(bal[ind]))
        elif c == 4:
            pin = int(input('Enter the new pin'))
            password[ind]=pin
        elif c == 5:
            print('Exit successful')
            break
        else:
            print('No correct choice TRY AGAIN')
