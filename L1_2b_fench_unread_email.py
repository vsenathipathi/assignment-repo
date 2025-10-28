# Fetch Unread emails and save email attachments to a local folder.
# 25-10-2025

import imaplib
import email # parses email messages into readable parts.
from email.header import decode_header
import os

from dotenv import load_dotenv
load_dotenv()
from_addr = os.getenv("EMAIL_USER")
password = os.getenv("EMAIL_PASS")

imap=imaplib.IMAP4_SSL('imap.gmail.com')
result=imap.login(from_addr,password)
# ('OK', [b'mailstovenkatesh@gmail.com authenticated (Success)'])
# imaplib.IMAP4.error: b'[AUTHENTICATIONFAILED] Invalid credentials (Failure)'

imap.select('"[Gmail]/All Mail"', readonly = True) 
response,messages=imap.search(None,'Unseen') # returns email IDs of all unread emails.
# print(messages)
# [b'3 74 78 79 80 81 82 83 84 85 86 87 88 89 90 93 94 95 100 101 117 118 119 121 309 443 444 445 446 523 524 559 579 580 585 605 606 607 608 609 610 611 613 614 615 618 620 621 623 624 626 627 628 632 634 635 637 640 641 643 644 650 651 652 653 654 659 660 664 665 668 670 671 672 673 674 677 678 679 680 681 682 683 687 689 690 694 695 700 704 705 706 707 721 722 724 725 726 727 728 729 730 731 732 734 735 736 737 738 739 742']
messages = messages[0].split() # [b'3', b'74', b'78', b'79', b'80', b'81', b'82']

latest = int(messages[-1])
oldest=int(messages[0])

for i in range(latest, latest-3, -1):
    # fetch
    res, msg = imap.fetch(str(i), "(RFC822)") # downloads full email content(h+b+att)
    
    for response in msg:
        if isinstance(response, tuple):
            msg = email.message_from_bytes(response[1])
            # print required information
            print(msg["Date"])
            print(msg["From"])
            print(msg["Subject"])

    for part in msg.walk():
        if part.get_content_type() == "text / plain":
            # get text or plain data
            body = part.get_payload(decode = True)
            print(f'Body: {body.decode("UTF-8")}', )

