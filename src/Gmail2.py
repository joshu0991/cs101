import smtplib
van_adres = 'cs101group7@gmail.com'
recipients = ['behmardibehrad@gmail.com','5712244794@vtext.com','7038699293@messaging.sprintpcs.com', 'joshualilly91@gmail.com']
recipients1 = ['zduric@gmu.edu',
               'zrajabi@gmu.edu',
               'thristov@gmu.edu']
message = 'Subject: {}\n\n{}'.format("YOU HAVE A MAIL",
                                     "Hello\n"
                                     "This message is From Group 7\n"
                                     "Thank You")
mail = smtplib.SMTP('smtp.gmail.com',587)
mail.ehlo()
mail.starttls()
mail.login(van_adres,'newpasswordcs101')
mail.sendmail(van_adres,recipients,message)
mail.close()