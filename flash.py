import sqlite3
import smtplib
import random
import os
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from flask import Flask, session, render_template, request, g

load_dotenv()

conn = sqlite3.connect('customer.db')
cur = conn.cursor()

app = Flask(__name__)


app.secret_key = "select_a_COMPLEX_secret_key_please"

@app.route("/", methods=["POST","GET"])


def home():
    conn = sqlite3.connect('customer.db')
    cur = conn.cursor()

    if request.method=="POST":
        email=request.form["email"]
        first_name=request.form["first_name"]
        last_name=request.form["last_name"]
        cur.execute("insert into customer (last_name, first_name , email) values(?, ?, ?)", [last_name, first_name , email]);



        sender_add='@gmail.com' #storing the sender's mail id
        receiver_add='@gmail.com' #storing the receiver's mail id
        password= os.getenv("password") #storing the password to log in
 #creating the SMTP server object by giving SMPT server address and port number
        smtp_server=smtplib.SMTP("smtp.gmail.com",587)
        smtp_server.ehlo() #setting the ESMTP protocol
        smtp_server.starttls() #setting up to TLS connection
        smtp_server.ehlo() #calling the ehlo() again as encryption happens on calling startttls()
        smtp_server.login(sender_add,password) #logging into out email id
#writing the message in HTML
        html_msg="""From: ABC
To: @gmail.com
MIME-Version: 1.0
Content-type: text/html
Subject:

"""
#sending the mail by specifying the from and to address and the message 
        smtp_server.sendmail(sender_add,receiver_add,html_msg)
        print('Successfully the mail is sent') #printing a message on sending the mail
        smtp_server.quit()#terminating the server
        return render_template("output.html", first_name =first_name, last_name=last_name, email=email)
    else:
        return render_template("index.html")

@app.route("/page")
def page():
    return "<h1> test </h1>"
if __name__ == '__main__':
    app.run()


