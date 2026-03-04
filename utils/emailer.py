import smtplib
from email.mime.text import MIMEText
from core.config import EMAIL, EMAIL_PASSWORD, RECEIVER

def send_email(body):

    msg = MIMEText(body)
    msg["Subject"] = "Daily Investment AI Report"
    msg["From"] = EMAIL
    msg["To"] = RECEIVER

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL, EMAIL_PASSWORD)
        server.sendmail(EMAIL, RECEIVER, msg.as_string())