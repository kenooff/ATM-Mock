Username = input ('what is your Username?\n')


AllowedUsers = ['Ken','Uju', 'Emeka']
AllowedPassword =['ZuriInternKen','ZuriInternUju','ZuriInternEmeka']




if(Username in AllowedUsers):
    Password = input ('your password? \n')
    UsernameId = AllowedUsers.index(Username)
                  
    if (Password == AllowedPassword[UsernameId]):

        print("welcome %s" % Username)
        import datetime
        now = datetime.datetime.now()
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        print('please select your preffered options')
        print('1. Withdrawal')
        print('2. Deposit')
        print('3. Complaint')

        selectedoption = int(input ('please select an option \n'))

        if (selectedoption == 1):
            
            print('you selected withdrawal')
            withdrawal = int(input('How much would you like to withdraw \n'))
            if (withdrawal >= 1):
                             
                print ('take your cash')
            else:
                print('enter an amount greater than 0')
                             
        
            pass
        elif(selectedoption == 2):
            deposit = int(input('How much would you like to deposit? \n'))
            
            print('your current balance is %s' % deposit)

            pass
        elif(selectedoption == 3):
            print('you selected complaint')
            input('What issue will you like to report? \n')
            print ('thank you for banking with us ')

            pass
        else:
            print('ínvalid option selected')


        
    else:
        print('íncorrect password, try again')

else:
    print('incorrect username, try again')
