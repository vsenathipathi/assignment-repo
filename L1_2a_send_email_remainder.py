# Send Automated email reminders with attachments
# 25-10-2025

import smtplib
from dotenv import load_dotenv
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

load_dotenv()
from_addr = os.getenv("EMAIL_USER")
password = os.getenv("EMAIL_PASS")
to_addr = os.getenv("TO_EMAIL") # TO_EMAIL=user1@gmail.com,user2@gmail.com
to_addrs=[]
for addr in to_addr.split(","):
    to_addrs.append(addr)
print(to_addrs)

def send_email_with_attachments(*failnames):


    msg  =MIMEMultipart() # Holds text content, attachments.
    msg["From"]=from_addr
    msg["To"]=",".join(to_addrs)
    msg["Subject"]="Subject - #1"

    body="""
    Hi User,<br> <br>
    Please find the attachement.<br><br>
    Regards,<br>
    Automated Emailer
    """
    msg.attach(MIMEText(body,'html'))

    # filename="data.csv"
    for filename in failnames:
        try:
            with open(filename,"rb") as attachment:
                p=MIMEBase('application','octet-stream') # for file
                p.set_payload(attachment.read()) # file bytes are loaded
                encoders.encode_base64(p) 
                p.add_header('Content-Disposition',f"attachment; filename={filename}")
                msg.attach(p)
        except FileNotFoundError:
            print(f"File {filename} not found")
            exit()

    # print(msg)
    with smtplib.SMTP('smtp.gmail.com',587) as s:
        try:
            s.starttls()
            s.login(from_addr,password)
            s.sendmail(from_addr,to_addrs,msg.as_string())
            print("Email sent successfully.")
        except smtplib.SMTPAuthenticationError:
            print("Login failed, check email/password")
        except smtplib.SMTPConnectError:
            print("failed to connect to SMTP")
        except smtplib.SMTPRecipientsRefused:
            print("Check for invalid address")
        except Exception as e:
            print(f"Unexpected error occured {e}")
            
send_email_with_attachments('data.csv','emp1.csv','emp.csv')
# import schedule
# import time
# # # send email using attachments
# schedule.every(1).minutes.do(send_email_with_attachments,'data.csv')

# while True:
#     schedule.run_pending()
#     time.sleep(1)
