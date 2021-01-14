#create an SMTP object, each object is used for connection with one server.

import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)

#Next, log in to the server
server.login("chandranitu@gmail.com", "Kalka@123")

#Send the mail
msg = "
Hello!" # The /n separates the message from the headers
server.sendmail("chandranitu@gmail.com", "chandranitu@gmail.com", msg)
