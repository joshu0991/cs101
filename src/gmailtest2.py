import os
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
COMMASPACE = ', '
def send_img():
    sender = 'cs101group7@gmail.com'
    gmail_password = 'newpasswordcs101'
    recipients = ['behmardibehrad@gmail.com','7038699293@messaging.sprintpcs.com','5712244794@vtext.com', 'joshualilly91@gmail.com']

    outer = MIMEMultipart()
    outer['Subject'] = 'EMAIL SUBJECT'
    outer['To'] = COMMASPACE.join(recipients)
    outer['From'] = sender
    outer.preamble = 'You will not see this in a MIME-aware mail reader.\n'
    attachments = ['tmp.png']
    message = 'Subject: {}\n\n{}'.format("YOU HAVE A MAIL",
                                         "Hello\n"
                                         "This message is From Group 7\n"
                                         "Thank You")
    for file in attachments:
        try:
            with open(file, 'rb') as fp:
                msg = MIMEBase('application', "octet-stream")
                msg.set_payload(fp.read())
            encoders.encode_base64(msg)
            msg.add_header('Content-Disposition', 'attachment', filename=os.path.basename(file))
            outer.attach(msg)
        except:
            print("Unable to open one of the attachments. Error: ", sys.exc_info()[0])
            raise
    composed = outer.as_string()
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as s:
            s.ehlo()
            s.starttls()
            s.ehlo()
            s.login(sender, gmail_password)
            s.sendmail(sender, recipients, composed)
            s.sendmail(sender, recipients, message)
            s.close()
    except:
        raise
send_img()
