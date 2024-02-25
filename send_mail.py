import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import socket

def send_email(subject, body):
    sender_email = "email address"
    receiver_email = "email address"
    password = "app password"

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())

def detect_intrusion():
    try:
        socket.create_connection(("127.0.0.1", 80), timeout=2)
    except Exception:
        send_email("Write massage here")
        print("The email has been sent.")

detect_intrusion()
