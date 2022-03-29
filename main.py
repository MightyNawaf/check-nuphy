from email.message import EmailMessage
import requests
from bs4 import BeautifulSoup
from termcolor import colored
import smtplib



# EMAIL SETUP
server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login("sender@gmail.com", "password")



# HTTP REQUEST
print(colored("Looking for you nuphy ... ", 'blue'))
r = requests.get('https://nuphy.com/collections/shop/products/nutype-f1?variant=32851509149805')
soup = BeautifulSoup(r.content, 'html.parser')



# MESSAGE DETAILS
msg = EmailMessage()
msg['From'] = "sender@gmail.com"
msg['To'] = "to@gmail.com"



# RED SWITCH
if(soup.getText().find("ISO - British / Black / Red Switch - Sold Out") != -1):
    print(colored('Red Switch ---- > Sorry, Not found', 'red'))
else:
    print(colored('Red Switch ---- > Yay, Found!', 'green'))
    # RED IS TRASH BTW
    # msg['Subject'] = 'Red Switch Found'
    # msg.set_content('Check it out : https://nuphy.com/collections/shop/products/nutype-f1?variant=32851509149805"')
    # server.send_message(msg)



# WHITE SWITCH
if(soup.getText().find("ISO - British / Black / White Switch - Sold Out") != -1):
    print(colored('White Switch ---- > Sorry, Not found', 'red'))
else:
    print(colored('White Switch ---- > Yay, Found!', 'green'))
    msg['Subject'] = 'White Switch Found'
    msg.set_content('Check it out : https://nuphy.com/collections/shop/products/nutype-f1?variant=32851509149805"')
    server.send_message(msg)



 # BROWN SWITCH
if(soup.getText().find("ISO - British / Black / Brown Switch - Sold Out") != -1):
    print(colored('Brown Switch ---- > Sorry, Not found', 'red'))
else:
    print(colored('Brown Switch ---- > Yay, Found!', 'green'))
    msg['Subject'] = 'Brown Switch Found'
    msg.set_content('Check it out : https://nuphy.com/collections/shop/products/nutype-f1?variant=32851509149805"')
    server.send_message(msg)


# QUIT CONNECTION
server.quit()
