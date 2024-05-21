import webbrowser#pip istall web-browser
url = 'https://www.youtube.com/shorts/SXHMnicI6Pg'

newpass = input("Make your new password:")
repass  = input("Confirm Your new Password:")

while True:
    if newpass == repass:
        print("password Set")
        break
    else:
        print("try-again")
        newpass = input("Make your new password:")
        repass  = input("Confirm Your new Password:")

xm = (newpass or repass)        

print("          ")

print("Login Your Account")

login = input("Enter your password")

if login == xm:
    print("login done")
else:
    print("retry")
    login == input("Enter your password")
    if login == xm:
        print("login done")
webbrowser.open(url)    




#to prank your friend make sure you cange the file name unless the will got youu
 #i am not doing it because i have no firends😒       



