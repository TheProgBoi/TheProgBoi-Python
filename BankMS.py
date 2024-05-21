import random
#This Video Will Contain 2 Parts THis Is Part One 
#In this Video I am going to make function-1,2,3,4
#function - 5,6,7, 8 Will be in part @
#Wlcome Backkkk 
#This Is Part 2 Today We Are going to make The function 5 6 7 8!!!!
#Lets Runn The Code
#NOte: I Have fixed Some Bugs Off camers!!!!!!!!!!!!!!!!!!!!!!!!
#new
money = 0
name = []
pwdmy = []
accnum = []
upi = []


while True:
   ch =  int(input("""
    ***Welcome To The Prog Bank***
            1-Open Account
            2-Deposit
            3-withdraw
            4-check Balance
            5-Make UPI
            6-Check Account
            7-Close Your Account
            8- Exit
            Enter Any One From This:  """))
   #Function One Done!!!
   if ch == 1:
      accname = input("ENter Your Full Name: ")
      accpwd = input("Make Your Password: ")
      accno = random.randint(1000000000, 9999999999)
      name.append(accname)
      pwdmy.append(accpwd)
      accnum.append(accno)
      print("Hurry! Your Account Is Created")  
      print("Here Are YOur Details:")
      print("Name: ", *name)
      print("Password: ", *pwdmy)
      print("Account NUmber", *accnum)
      #Function 2 Done
   
   elif ch == 2:
    reno = int(input("Enter YOur Account Number : "))
    if reno == accno:
      print("Welcome", *name)
      dpm = int(input("Enter MOney To deposit: "))
      money+=dpm
      print("Your Total Balance Is :", money)
    else:
      print("try Again")
      reno = int(input("Enter YOur Account Number : "))

      #function 3 done
   elif ch == 3:
     reno = int(input("Enter YOur Account Number : "))
     if reno == accno:
       print("Welcome", *name)
       wpm = int(input("Enter Money To WithDraw: "))
       money-=wpm
       print("Your Total Balance Is: ", money)


     else:
       print("Try Again:") 
       reno = int(input("Enter YOur Account Number : "))
     
     #function 4 DOne
   elif ch == 4:
     reno = int(input("Enter YOur Account Number : "))
     if reno == accno: 
       print("Welcome", *name)
       print("Here Is Your Total Balance: ", money) 
     else:
       print("Try Again:") 
       reno = int(input("Enter YOur Account Number : "))

   elif ch == 5:
     reno = int(input("Enter YOur Account Number : "))
     if reno == accno: 
       print("Welcome", *name)
       upid = random.randint(1000000000, 9999999999)
       upi.append(upid)
       print("Yaay Your Upi Id Is created!!")
       print("Here IS it:", *upi, "@bros",  sep="")
     else:
       print("try Again")
       reno = int(input("Enter YOur Account Number : "))  

   elif ch == 6:
     reno = int(input("Enter YOur Account Number : "))
     if reno == accno: 
       print("Welcome", *name)
       print("Here Are YOur Details:")
       print("Name: ", *name)
       print("Upi:", *upi, "@bros", sep="")
       # PRogBOi is a lazy Man hahahaha
       print("Password: ", *pwdmy)
       print("Account NUmber", *accnum)
     else:
       print("Try Again")
       reno = int(input("Enter YOur Account Number : "))
       #HAve The Same Happend With You😂😂😂😂
         
   elif ch == 7:
     reno = int(input("Enter YOur Account Number : "))
     if reno == accno: 
       print("Welcome", name)
       ca = input("Are You Sure To close Your Account If Yes Type y or Y or No type n or N:")
       if 'y' in ca.lower():
         name.clear()
         upi.clear()
         accnum.clear()
         pwdmy.clear()
         money = 0 

       else:
         print("Thanks")
         continue

   elif ch == 8:
     ex = input("Are You Sure To Exit If Yes Type y or Y or No type n or N:")
     if 'y' in ex.lower():
       print('Exiting....')
       print("Exited!")
       break
     else:
       continue
       
       
     
          
          

          
           

     
     
       
     

       



    #THE CODE IS oK BUT I AM HAVING A DOUBT THAT WHENEVR IN IF RENO == ACCNUM IT GIVES ME TRY AGAIN I WILL GIVE SHOUTOUT WHO WILL FIX THIS AND TEACH ME
    #RIGHT NOW I CANT GIVE SOURCE CODE TO YOU BUT IN 2 PART ILL GIVE
    # @THEPROGBOI69
     




    


