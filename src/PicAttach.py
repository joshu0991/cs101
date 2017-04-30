import smtplib
import mimetypes
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.message import Message
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.text import MIMEText

emailfrom = 'cs101group7@gmail.com'
recipients = ['behmardibehrad@gmail.com','7038699293@messaging.sprintpcs.com','5712244794@vtext.com', 'joshualilly91@gmail.com']
emailto = recipients
fileToSend = "1.jpg"

msg = MIMEMultipart()
msg["From"] = emailfrom
msg["To"] = emailto
msg["Subject"] = "help I cannot send an attachment to save my life"
msg.preamble = "help I cannot send an attachment to save my life"

fp = open(fileToSend, 'rb')
img = MIMEImage(fp.read())
fp.close()
img.add_header('Content-ID', '<{}>'.format(fileToSend))
msg.attach(img)
print(msg.as_string())


server = smtplib.SMTP("smtp.gmail.com:587")
server.starttls()
server.login(emailfrom,'newpasswordcs101')
server.sendmail(emailfrom, emailto, msg.as_string())
server.quit()