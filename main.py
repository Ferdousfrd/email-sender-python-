#email sender with python
#step1: gotta go gmail acount and setup 2 factor authentication
#step2: generate app pasword
#step3: create a function to send mail


# Import necessary libraries

from email.message import EmailMessage  # Importing EmailMessage class to construct email messages
import ssl  # Importing SSL for secure connection
import smtplib  # Importing smtplib for sending emails

# Gmail sender email address and app password

email_sender = "ferdous.frd81@gmail.com"
email_password = "ksev jcxj npmh eldx"

#getiing user name and emailaddress

personName = input("Please enter the reciever name_\n")
email_reciever = input("Please give the email address!\n")

subject = "Valentines Special <3 "

body = f"""
Hello, {personName}!
With due respect, I would like to state that, due to strikes and busy school schedule, it 
is not very likely that we can go on a coffee date as your awesome amazing cooz batman
 super hero+villain boyfriend planned. Still on the board so negotiatable.
 
So, malady, would you be down to have a board games, some wine and and cozy candle night dinner at your place?
We can also dance do some salsa when the wine kicks in.  \n

Yours truly,
The king and slayer of dragons,
Ferdous the mighty!
"""

#trying to change part of email body

def changingMsgParts(str):
    wordsToChange = input("What words or lines you want to change?\n")
    wordsThatReplaces = input("New words that replaces old ones..\n")
    modified_str = str.replace(wordsToChange, wordsThatReplaces)
    return modified_str

#function to send the email

def sendingMail():
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_reciever, em.as_string())

# Prompt user for choice
        
choice = int(input("press 1 for changing email or 2 for send same email!\n"))

if choice == 1:

    body = changingMsgParts(body)

    # Create EmailMessage object
    em = EmailMessage()
    em["From"] = email_sender
    em["To"] = email_reciever
    em["subject"] = subject
    em.set_content(body)

    sendingMail()    # Sending the email

else:
    
    # Create EmailMessage object
    em = EmailMessage()
    em["From"] = email_sender
    em["To"] = email_reciever
    em["subject"] = subject
    em.set_content(body)

    sendingMail()    # Sending the email



