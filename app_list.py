import speech_recognition as sr
import smtplib
import pyaudio
import platform
import sys
from bs4 import BeautifulSoup
import email
import imaplib
from imap_tools import A
from gtts import gTTS
import pyglet
import os, time

print ("~"*60)
print ("       Voice based Email for visually challenged people")
print ("~"*60)

#project name
ts = gTTS(text="Voice based Email for visually challenged people", lang='en')
tsname=("name.mp3")
ts.save(tsname)

music = pyglet.media.load(tsname, streaming = False)
music.play()

time.sleep(music.duration)
os.remove(tsname)

#below code is for giving credentials as input
'''
r0 = sr.Recognizer()
with sr.Microphone() as source:
    print ("Enter Username")
    t1 = gTTS(text="Enter Username.", lang='en')
    t1_id=("person1.mp3")
    t1.save(t1_id)
    music = pyglet.media.load(t1_id, streaming = False)
    music.play()
    time.sleep(music.duration)
    l1 = r0.listen(source)
    login_name = r0.recognize_google(l1)
    login_id = open("login_id.txt",'w+')
    login_id.write(login_name)
    login_id.close()
    print(login_name)
    os.remove(t1_id)

    print ("Enter Password")
    t2 = gTTS(text="Enter Password.", lang='en')
    t2_id=("person2.mp3")
    t2.save(t2_id)
    music = pyglet.media.load(t2_id, streaming = False)
    music.play()
    time.sleep(music.duration)
    l2 = r0.listen(source)
    login_pwd = r0.recognize_google(l2)
    login_pass = open("login_pass.txt",'w+')
    login_pass.write(login_pwd)
    login_pass.close()
    print(login_pwd)
    os.remove(t2_id)

    print ("Enter Receiver name")
    t3 = gTTS(text="Enter Receiver name.", lang='en')
    t3_id=("person3.mp3")
    t3.save(t3_id)
    music = pyglet.media.load(t3_id, streaming = False)
    music.play()
    time.sleep(music.duration)
    l3 = r0.listen(source)
    send_name = r0.recognize_google(l3)
    send_id = open("send_id.txt",'w+')
    send_id.write(send_name)
    send_id.close()
    print(send_name)
    os.remove(t3_id)
'''
login_id = open("login_id.txt",'r')
login_pass = open("login_pass.txt",'r')
send_id = open("send_id.txt",'r')
#login from os
login = os.getlogin
print ("You are logged In from : "+login())
#lg = gTTS(text="You are logged in from ," + login_id.read())

#choices
print ("0. Compose a mail.")
ts = gTTS(text="option 0. Compose a mail.", lang='en')
tsname=("hello.mp3")
ts.save(tsname)
music = pyglet.media.load(tsname, streaming = False)
music.play()
time.sleep(music.duration)
os.remove(tsname)

print ("1. Check your inbox")
ts = gTTS(text="option 1. Check your inbox", lang='en')
tsname=("hello.mp3")
ts.save(tsname)
music = pyglet.media.load(tsname, streaming = False)
music.play()
time.sleep(music.duration)
os.remove(tsname)

#this is for input choices
ts = gTTS(text="Your choice ", lang='en')
tsname=("hello.mp3")
ts.save(tsname)
music = pyglet.media.load(tsname, streaming = False)
music.play()
time.sleep(music.duration)
os.remove(tsname)

#voice recognition part
r = sr.Recognizer()
with sr.Microphone() as source:
    print ("Your choice:")
    audio=r.listen(source)
    print ("ok done!!")

try:
    text=r.recognize_google(audio)
    print ("You said : "+text)

except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio.")
    ex = gTTS(text="Please , try again.")

except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
    ex = gTTS(text="Please , try again.")

if int(text) == 0:
    r = sr.Recognizer()                                                                     
    with sr.Microphone() as source:
        print ("Your message :")
        audio=r.listen(source)
        print ("ok done!!")
    try:
        text1=r.recognize_google(audio)
        print ("You said : "+text1)
        msg = text1
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio.")
        ex = gTTS(text="Please , try again.")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        ex = gTTS(text="Please , try again.")

    mail = smtplib.SMTP('smtp.gmail.com',587)
    mail.ehlo()
    mail.starttls()


    login_name = login_id.read()
    login_pwd = login_pass.read()
    send_name = send_id.read().split(',')

    mail.login(login_name + "@gmail.com",login_pwd)                                                                             #login section
    for i in range(len(send_name)):
        mail.sendmail(login_name + "@gmail.com",send_name[i] + "@gmail.com",msg)                                                 #send section
    print ("Your mail has been sent. ")
    ts = gTTS(text="Your mail has been sent. ThankYou.", lang='en')
    tsname=("send.mp3")
    ts.save(tsname)
    music = pyglet.media.load(tsname, streaming = False)
    music.play()
    time.sleep(music.duration)
    os.remove(tsname)
    mail.close()

if int(text) == 1:
    mail = imaplib.IMAP4_SSL('imap.gmail.com',993)
    login_name = login_id.read()
    login_pwd = login_pass.read()                                          
    unm = (login_name)                                                        
    psw = (login_pwd)                                                                     
    mail.login(unm,psw)                                                                  
    stat, total = mail.select('Inbox')                                                   
    print ("Number of mails in your inbox :"+str(total))
    ts = gTTS(text="Total mails are :"+str(total), lang='en')                            
    tsname=("total.mp3")
    ts.save(tsname)
    music = pyglet.media.load(tsname, streaming = False)
    music.play()
    time.sleep(music.duration)
    os.remove(tsname)
    #unseen mails
    unseen = mail.search(None, 'Unseen')
    unseen = str(unseen[1])
    unseen = unseen.split()                                                       
    print ("Number of Unseen mails :"+str(len(unseen)))
    ts = gTTS(text="Your Unseen mail :"+str(len(unseen)), lang='en')
    tsname=("unseen.mp3")
    ts.save(tsname)
    music = pyglet.media.load(tsname, streaming = False)
    music.play()
    time.sleep(music.duration)
    os.remove(tsname)

    #search mails
    result, data = mail.uid('search',None, "ALL")
    inbox_item_list = data[0].split()
    new = inbox_item_list[-1]
    old = inbox_item_list[0]
    result2, email_data = mail.uid('fetch', new, '(RFC822)')                                #fetch
    raw_email = email_data[0][1].decode("utf-8")                                            #decode
    email_message = email.message_from_string(raw_email)
    print ("From: "+email_message['From'])
    print ("Subject: "+str(email_message['Subject']))
    ts = gTTS(text="From: "+email_message['From']+" And Your subject: "+str(email_message['Subject']), lang='en')
    tsname=("mail.mp3")
    ts.save(tsname)
    music = pyglet.media.load(tsname, streaming = False)
    music.play()
    time.sleep(music.duration)
    os.remove(tsname)
    #Body part of mails
    stat, total1 = mail.select('Inbox')
    #stat, data1 = mail.fetch(total1[0],A(all = True))
    #msg = data1[0][1]
    msg = email.message_from_string(raw_email)
    #txt = ""
    if msg.is_multipart():
        for part in msg.walk():
            ctype = part.get_content_type()
            cdispo = str(part.get('Content-Disposition'))

        # skip any text/plain (txt) attachments
            if ctype == 'text/plain' and 'attachment' not in cdispo:
                txt = part.get_payload(decode=True)  # decode
                break

    else:
        txt = msg.get_payload(decode=True)
    #soup = BeautifulSoup(msg, "html.parser")
    #txt = soup.get_text()
    print ("Body :"+txt.decode('utf-8'))
    ts = gTTS(text="Body: "+txt.decode('utf-8'), lang='en')
    tsname=("body.mp3")
    ts.save(tsname)
    music = pyglet.media.load(tsname, streaming = False)
    music.play()
    time.sleep(music.duration)
    os.remove(tsname)
    mail.close()
    mail.logout()