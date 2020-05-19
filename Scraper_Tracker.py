#OS Tracker for Scraper Files
import os.path
import time
import smtplib, ssl
#user credentials in config.py:
import config

today = time.ctime()[4:10]

def sendMail(subject, mail_content):
    #import User credentials  for login from config.py
    sender_address = config.emailaddress
    sender_pass = config.password

    session = smtplib.SMTP('smtp.gmail.com:587') #use gmail with port
    session.ehlo()
    session.starttls()
    session.login(sender_address, sender_pass) #login with mail_id and password
    message = 'Subject: {}\n\n{}'.format(subject, mail_content)
    session.sendmail(sender_address, sender_address, message)
    session.quit()
    #print('Mail Sent')

def tracker():
    #getting the time when file was updated last
    mT_IndeedEinkauf = time.ctime(os.path.getmtime(r'C:\Users\...\Einkauf\CompanyJobs.xlsx'))[4:10]
    mT_IndeedSoftware = time.ctime(os.path.getmtime(r'C:\Users\...\Softwareentwickler\CompanyJobs.xlsx'))[4:10]
    mT_IndeedPython = time.ctime(os.path.getmtime(r'C:\Users\...\Python Entwickler\CompanyJobs.xlsx'))[4:10]

    #checking if every file is updated and send mail
    if mT_IndeedEinkauf == mT_IndeedSoftware == mT_IndeedPython == today:
        subject = 'Everything updated! ' + str(today)
        mail_content = 'Everything updated from Indeed! Einkauf: ', mT_IndeedEinkauf, ', Software: ', mT_IndeedSoftware, ', Python Developer: ', mT_IndeedPython
        sendMail(subject, mail_content)

    else:
        subject = 'There was a problem - please check ' + str(today)
        mail_content = 'There was problem: IndeedEinkauf: ', mT_IndeedEinkauf, ', IndeedSoftware: ', mT_IndeedSoftware, ', Python Developer: ', mT_IndeedPython
        sendMail(subject, mail_content)


tracker()
