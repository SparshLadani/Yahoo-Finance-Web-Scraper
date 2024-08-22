import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def send(filename):
    from_email = input("Enter an email address from which you want to send a mail: ")
    to_email = input("Enter an email address to which you want to send a mail: ")

    from_add = from_email
    to_add = to_email
    subject = "Today's Finance Report"

    msg = MIMEMultipart()
    msg['From'] = from_add
    msg['To'] = to_add
    msg['Subject'] = subject

    body = "<b>Today's Finance Stats of Amazon, Alphabet, Microsoft and Cognizant attached below.</b>"
    msg.attach(MIMEText(body, 'html'))

    my_file = open(filename, 'rb')

    part = MIMEBase('application', 'octet-stream')
    part.set_payload((my_file).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename= ' + filename)
    msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login( from_add, 'xztufnjqaoqfmbbp')

    message = msg.as_string()
    server.sendmail(from_add, to_add, message)
    server.quit()
