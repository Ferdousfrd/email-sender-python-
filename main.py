#email sender with python

#step1: gotta go gmail acount and setup 2 factor authentication
#step2: generate app pasword
#step3: create a function to send mail

#import email and libraries
from email.message import EmailMessage
import ssl
import smtplib

email_sender = "ferdous.frd81@gmail.com"
email_password = "ksev jcxj npmh eldx"

email_reciever = "viktoriia.martynenko@tuni.fi"

subject = "Valentines Special <3 "
body = """
Hello!
With due respect, I would like to state that, due to strikes and busy school schedule, it 
is not very likely that we can go on a coffee date as your awesome amazing cooz batman
 super hero+villain boyfriend planned. Still on the board so negotiatable.
 
So, malady, would you be down to have a board games, some wine and and cozy candle night dinner at your place?
We can also dance do some salsa when the wine kicks in.  

Yours truly,
The king and slayer of dragons,
Ferdous the mighty!
"""

em = EmailMessage()
em["From"] = email_sender
em["To"] = email_reciever
em["subject"] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_reciever, em.as_string())
