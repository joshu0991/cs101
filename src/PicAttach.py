from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText  # Added
from email.mime.image import MIMEImage

attachment = 'bob.jpg'

msg = MIMEMultipart()
msg["To"] = 
msg["From"] = from
msg["Subject"] = subject

msgText = MIMEText('<b>%s</b><br><img src="cid:%s"><br>' % (body, attachment), 'html')
msg.attach(msgText)   # Added, and edited the previous line

fp = open(attachment, 'rb')
img = MIMEImage(fp.read())
fp.close()
img.add_header('Content-ID', '<{}>'.format(attachment))
msg.attach(img)

print msg.as_string()
exit(0)