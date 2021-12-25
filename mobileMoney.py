# Transaction using Mobile money;
def Mobile_money():
    print(" Dear customer,welcome to Airtel money")

    amount = 100000
    pin = 4532
    
    print("1. Send money")
    print("2. Withdraw cash")
    print("3. Airtime/bundles")
    print("4. My account")
    choice=int(input("enter your choice: "))

    # Selecting send money option
    if choice == 1:
        print("Send Money")
    
        print("1. Airtel and other number")
        print("2. MTN")
        choic=int(input("choose the network: "))
    
        # Selecting Airtel for sending
        if choic == 1:
             

            Airtel = int(input("enter airtel number: "))
            send_money = int(input("enter the amount to send: "))
            send_charges = 0.11*send_money
            print("Sending ",send_money,"to",Airtel, "with a charge of",send_charges,".please enter your pin to confirm")
            print("1. enter your pin")
        
            put_pin = int(input("enter your 4 digit pin: "))
            balance = amount - send_money - send_charges
            if put_pin == pin and send_money > 500 and balance > 0:
                print("you have successfully sent",send_money,"shs to", Airtel, "with a charge of",send_charges,"shs and your new balance is",balance,"shs")

            elif  put_pin != pin:
                 print("Invalid pin number. Please retry")
            elif  send_money < 500:
                print("The amount is too low to be sent. The balance must be above 500")
            
            else:
                print("Dear customer, you do not have sufficient funds on your account.add money and try again")
       

        
            
        # Selecting MTN for sending
        elif choic == 2:
            
      
            MTN = int(input("enter MTN number"))
            send_money = int(input("enter the amount to send: "))
            send_mtncharges = 0.25 * send_money
            print("Sending ",send_money,"to",MTN, "with a charge of",send_mtncharges,".please enter your pin to confirm")
            print("1. enter your pin")
          
            put_pin = int(input("enter your 4 digit pin: "))
            balanc = amount-send_money-send_mtncharges
            if put_pin == pin and send_money > 1000 and balanc > 0:
                print("you have successfully sent",send_money,"shs to", MTN, "with a charge of",send_mtncharges,"shs and your new balance is",balanc,"shs")
            elif  put_pin != pin:
                print("Invalid pin number.Please retry")

            elif  send_money < 1000:
                print("The amount is too low to be sent. the balance must be above 1000")

            else:
                print("Dear customer, you do not have sufficient funds on your account.add money and try again")

        else:
            print("Invalid input.Please retry")
       
    # Selecting withdraw cash option

    elif choice == 2:
        withdraw = int(input("enter amount to withdraw: "))
        print("1. enter your 4 digit pin")
        picked_pin = int(input("enter your pin: "))
        withdraw_charges = 0.1 * withdraw
        bal = amount - withdraw - withdraw_charges
        if picked_pin == pin and withdraw >= 1200 and withdraw < amount:
        
            print("you have successfully withdrawn ",withdraw," shs with a charge of",withdraw_charges, " shs and your current balance is",bal,"shs")

        elif picked_pin != pin:
            print("invalid pin number. please retry")
        elif withdraw < 1200:
            print("The amount is too low to be withdrawn. you should withdraw atleast 1200")
         
        else:
            print("Dear customer, you do not have sufficient funds on your account.add money and try again")
        
    # Selecting Airtime/Bundles Option
    elif choice == 3:
        print("Airtime/Bundles")
        print("1. Airtime")
        print("2. Bundles")
        select = int(input("enter your selection: "))
        if select == 1:
            print("1. for myself")
            print("2. for another number")
            sel=int(input("enter your choice: "))
            # Selecting Airtime option
            if sel == 1:
                airtime = int(input("enter airtime: "))
                blance = amount - airtime
            
                pin_no = int(input("enter pin: "))
                if pin_no == pin and airtime <= amount and airtime > 10:
                    print("You have successfully bought airtime of",airtime,"shs and your balance is",blance,"shs")
                elif pin_no != pin:
                    print("Invalid pin.Try again later")

                elif airtime <= 10:
                    print("Airtime must be above 10")

                else:
                    print("you have insufficient funds")

            elif sel == 2:
            

                phone_number = int(input("enter phone number: "))
                airtyme = int(input("enter airtime: "))
            
                pin_numbe = int(input("enter pin: "))
                balnce = amount - airtyme
                if pin_numbe == pin and airtyme <= amount and airtyme > 10: 
                    print("You have successfully bought airtime of",airtyme,"to",phone_number," and your balance is",balnce,"shs")

                elif pin_numbe != pin:
                    print("Invalid pin")
                
                elif airtyme <= 10:
                    print("you can only buy airtime above 10 shs")
                
           
                
                else:
                    print("you have insufficient funds")
            else:
                print("Invalid input.please try again")
        
        
        # Selecting data option
        elif select == 2:
            print("1. buy for self")
            print("2. buy for other number")
            sel_ct = int(input("choose an option: "))

            if sel_ct == 1:

            
                print("1. 100mbs for 2000")
                print("2. 500mbs for 5000")
                mb = int(input("enter data: "))
                pinNumber = int(input("enter pin number: "))
            

                if mb == 1 and pinNumber == pin:
                    balance_remaining = amount - 2000

                
                
               
                    print("you have bought 100 mbs and your balance is",balance_remaining,"shs")
                

                elif mb == 2 and pinNumber == pin:
                
                    balance_remain = amount - 5000
                    print("you have bought 500mbs and your balance is",balance_remain,"shs")
              
            
            if sel_ct == 2:
            
                phone_numb = int(input("enter the phone number: "))

           
                print("1. 100mbs for 2000")
                print("2. 500mbs for 5000")
                mbs = int(input("enter data: "))
                pinNumb = int(input("enter pin number: "))
                if mbs == 1 and pinNumb == pin:
                    balance_left = amount - 2000
                    print("you have bought 100 mbs to",phone_numb," and your balance is",balance_left,"shs")
                elif mbs == 2 and pinNumb == pin:
                    balance_rem=amount-5000
                    print("you have bought 500mbs and your balance is",balance_rem,"shs")
                else:
                    print("Invalid input")
            else:
                print("Invalid input")
        else:
            print("Invalid input")

    # Selecting Account Option
    elif choice == 4:
        print("my account")
        print("1. my pin")
        print("2. checkbalance")
        option=int(input("enter option"))
        if option == 1:
            print(pin)
        elif option == 2:
            print(amount)
        else:
            print("wrong input")




    else:
        print("Invalid input")

Mobile_money()
                
           


          




            

               


        
        
        
        
        
        
      
         
           
       
          
    
        
        
        
      
        
        
        
      
            

        
        

           
            
            
        
           
       
         
            
            
            

