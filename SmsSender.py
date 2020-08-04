print("""

 ____  _      ____    ____  _____ _      ____  _____ ____ 
/ ___\/ \__/|/ ___\  / ___\/  __// \  /|/  _ \/  __//  __\
|    \| |\/|||    \  |    \|  \  | |\ ||| | \||  \  |  \/|
\___ || |  ||\___ |  \___ ||  /_ | | \||| |_/||  /_ |    /
\____/\_/  \|\____/  \____/\____\\_/  \|\____/\____\\_/\_\
                                                          

""")
from twilio.rest import Client
import time
import pymsgbox
cod = "1"
msg = "Hello"
cod = "+" + cod
numbar = sum(1 for line in open('phonelist.txt'))
time.sleep(4)
fayl = open("phonelist.txt" ,'r')
time.sleep(4)
# Your Account SID from twilio.com/console
account_sid = "ACd0f1568b5d0c8008b563c6742b9ed37e"
# Your Auth Token from twilio.com/console
auth_token  = "e1600a8f853cc475d1be92544d1dc892"
for i in range(0,numbar):
    time.sleep(3)
    recipent = cod + str(fayl.readline())
    print(str(recipent))
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    to= recipent, 
    from_="+12146236099",
    body= msg)
    print(message.sid)
    print("SMS Sent Success!")
    time.sleep(1)
