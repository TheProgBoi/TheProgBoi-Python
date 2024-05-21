def attendence():
    while True:
        totalclass = int(input("Enter The Total Classes: "))
        attendedclasses = int(input("Enter The Class Attended By you:"))
        percentage = (attendedclasses/totalclass)* 100

        minimumattendence = 75

        if percentage >=minimumattendence:
            print("You Can give Exam")
            break
        else:
            print("You cant give exam")

        cause = input("Do you have to take leave because of any MEDICAL CAUSE? //if Yes Type :y: or :Y:>>>")

        if 'y' in cause or 'Y' in cause:
            print("You can give exam /Show documents to office/")
            break
            
        else:
            if percentage >=minimumattendence:
                print("Allowed To give Exam")
                break
            else:
                print("Not allowed to give exam")

attendence()                        
